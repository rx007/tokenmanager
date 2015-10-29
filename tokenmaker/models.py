from django.db import models
from tokenmaker import settings
from tokenmaker.utils import token_issue_by_password
import requests
import datetime

# Create your models here.

TOKEN_STATUS_CHOICES = (
    (0, 'avaliable'),
    (1, 'not avaliable'),
)

class TokenManager(models.Manager):

    def new_token(self, username=None, password=None):
        # r = token_issue_by_password(username=None, password=None)
        try:
            token = self.get_current_token()
            token.token_previous = token.token
        except:
            token = Token()
            token.token_previous = ""
        
        # token.token = r["access"]["token"]["id"]
        # token.issued_datetime = datetime.datetime.now(datetime.timezone.utc)
        # token.expires_datetime = datetime.datetime.strptime(
        #         r["access"]["token"]["expires"],
        #         settings.ISO8691_DATETIME_FORMAT)
        # token.by_user = username
        # token.save()
        token.issue()
        return token

    def get_current_token(self):
        return Token.objects.last()

    def get_avaliable_token(self):
        latest = Token.objects.last()
        if not latest.is_avaliable():
            raise Exception("Token not avaliable anymore!")
        return latest

        

class Token(models.Model):

    token = models.CharField(max_length=36)
    token_previous = models.CharField(max_length=36, null=True, blank=True)
    issued_datetime = models.DateTimeField()
    expires_datetime = models.DateTimeField()
    by_user = models.CharField(max_length=40)
    status = models.IntegerField(default=0, choices=TOKEN_STATUS_CHOICES)

    objects = TokenManager()

    def is_avaliable(self):
        return self.expires_datetime > datetime.datetime.now(datetime.timezone.utc)

    def is_refreshable(self):
        return self.expires_datetime > datetime.datetime.now(datetime.timezone.utc)

    def refresh(self):
        if not self.is_refreshable():
            raise Exception("Token is not refreable anymore!")
        return self.issue()

    def issue(self):
        r = token_issue_by_password(username=None, password=None)
        self.token_previous = self.token
        self.token = r["access"]["token"]["id"]
        self.expires_datetime = datetime.datetime.strptime(
                r["access"]["token"]["expires"],
                settings.ISO8691_DATETIME_FORMAT
                )
        self.issued_datetime = datetime.datetime.now(datetime.timezone.utc)
        self.save()
        return self
