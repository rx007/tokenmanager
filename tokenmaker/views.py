from django.shortcuts import render
from django.views.generic import FormView, DetailView, View
from tokenmaker.models import Token
from tokenmaker.forms import TokenForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from tokenmaker.tasks import *
from datetime import datetime, timedelta

# Create your views here.

class TokenDetailView(DetailView):
    template_name = "tokenmaker/detail.html"

    def get_object(self):
        try:
            token = Token.objects.get_avaliable_token()
        except:
            token = Token.objects.new_token()
        return token

class TokenIssueView(View):
    def get(self, request, *args, **kwargs):
        Token.objects.new_token()
        return HttpResponseRedirect(reverse('token_detail'))
        

# class TokenFormView(FormView):
#     template_name = "tokenmaker/update.html"
#     form_class = TokenForm
#
#     def form_valid(self, form):
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#
#         Token.objects.new_token(username, password)
#         token_refresh.apply_async(
#                 eta=datetime.utcnow() + timedelta(minutes=1)
#                 )
#         return HttpResponseRedirect(self.get_success_url())
#
#     def get_success_url(self):
#         return reverse('token_detail')

class TokenDetailAPIView(View):
    def get(self, request, *args, **kwargs):
        try:
            token = Token.objects.get_avaliable_token()
        except:
            token = Token.objects.new_token()
        return token
        
