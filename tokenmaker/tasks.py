from __future__ import absolute_import

from celery import shared_task
from tokenmaker.models import Token
from datetime import datetime, timedelta


# @shared_task
# def token_refresh():
#     token = Token.objects.get_avaliable_token()
#     token.refresh()
#     token_refresh.apply_async(
#             eta=datetime.utcnow() + timedelta(minutes=1)
#             )
#     return
