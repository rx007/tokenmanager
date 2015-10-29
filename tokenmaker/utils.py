import requests
from tokenmaker import settings
TOKEN_ISSUE_HEADER = {
        "Content-Type": "application/json",
        "Accept": "application/json"
        }

def token_issue_by_password(username=None, password=None):
    if username == None:
        username = settings.OPENSTACK_USERNAME
        password = settings.OPENSTACK_PASSWORD
    payload = {
            "auth": {
                "tenantName": settings.OPENSTACK_TENANT,
                "passwordCredentials": {
                    "username": username,
                    "password": password
                    }
                }
            }
    res = requests.post(
            settings.OPENSTACK_URL, 
            headers = TOKEN_ISSUE_HEADER,
            json = payload
            ).json()
    return res

def token_issue_by_token(token):
    payload = {
            "auth": {
                "tenantName": settings.OPENSTACK_TENANT, 
                "token": {
                    "id": token
                    }
                }
            }
    res = requests.post(
            settings.OPENSTACK_URL, 
            headers = TOKEN_ISSUE_HEADER,
            json = payload
            ).json()
    return res
