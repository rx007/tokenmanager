import os
OPENSTACK_URL = "http://dev.api.openstack.iaas.prod.jp.local:5000/v2.0/tokens"
ISO8691_DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

OPENSTACK_REFRESH_TYPE = "PASSWORD" # or "TOKEN"
OPENSTACK_TENANT = "chef"
OPENSTACK_USERNAME = os.environ['OPENSTACK_USERNAME']
OPENSTACK_PASSWORD = os.environ['OPENSTACK_PASSWORD']
