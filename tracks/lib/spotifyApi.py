from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search(token, q=[], _type=(), limit=None, offset=None, sort_parameter=None, reverse=False):   
    url = 'https://api.spotify.com/v1/search?'

    for count, parameter in enumerate(q):
        if count == 0:
            url += 'q='
        url += parameter[0] + ':' + parameter[1]
    for parameter in _type:
        if count == 0:
            url += '&type='
        else:
            url += ','
        url += parameter
    if limit:
        url += f'&limit={limit}'
    if offset:
        url += f'&offset={offset}'

    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]["items"]
    if sorted:
        json_result = sorted(json_result, key=lambda x: x[sort_parameter], reverse=reverse)
    return json_result

