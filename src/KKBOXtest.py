import json

from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
import requests
import csv

from jsonConverter import jsonConverter


def request():
    # Authentication with oAuth2 to retreive token for API call
    auth = HTTPBasicAuth('9571aa9d158897b1e31bf2bcdb35b6a1', 'd8b577993562cbc222b5789115361e3c')
    client = BackendApplicationClient(client_id='9571aa9d158897b1e31bf2bcdb35b6a1')
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url='https://account.kkbox.com/oauth2/token', auth=auth)['access_token']
    print(token)

    endpoint = 'https://api.kkbox.com/v1.1/charts/8om53R0PWzFpUw-JkL?territory=TW'
    headers = {"Authorization": "Bearer {}".format(token)}
    response = requests.get(endpoint, headers=headers).json()
    #print(response)
    out_file = open("kkboxtest.json", "w")
    json.dump(response, out_file, indent=6)

    out_file.close()

    result = []
    rank = 1
    for item in response["tracks"]["data"]:
        result.append([str(rank), item['album']['artist']['name'], item["album"]["name"], item["name"]])
        rank += 1
    header = ["Rank", "Artist Name", "Album Name", "Track Name"]

    with open('kkboxtest.json', 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(result)
    print('Done!')
request()