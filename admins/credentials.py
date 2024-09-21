import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64


class Credentials:
    consumer_key = 'HV2y77i48VogFcYIYwXDkiuizwuCNv74OpAXUJaSQncQ3VTH'
    secret_key = '75sHTfVtuAhGi25LubKqwXJiHyyzoEc3ja4sstB11GCNwaBt4AhWQdmkZQZKlgsa'
    pass_key = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
    api_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credential'


class MpesaAccessToken:
    push = requests.get(Credentials.api_url, auth=HTTPBasicAuth(Credentials.secret_key, Credentials.consumer_key))
    access_token = json.loads(push.text)
    validated_access_token = access_token['access_token']
