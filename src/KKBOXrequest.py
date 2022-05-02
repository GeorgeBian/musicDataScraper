import json
import csv

from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
import requests
from jsonConverter import jsonConverter

class KKBOXrequest:
        def __init__(self, client_id=r'9571aa9d158897b1e31bf2bcdb35b6a1', client_secret=r'd8b577993562cbc222b5789115361e3c'):
                self.client_id = client_id
                self.client_secret = client_secret
        def request(self, tracklist_id, fileName):
                #Authentication with oAuth2 to retreive token for API call
                try:
                        # Authentication with oAuth2 to retreive token for API call
                        auth = HTTPBasicAuth('9571aa9d158897b1e31bf2bcdb35b6a1', 'd8b577993562cbc222b5789115361e3c')
                        client = BackendApplicationClient(client_id='9571aa9d158897b1e31bf2bcdb35b6a1')
                        oauth = OAuth2Session(client=client)
                        token = oauth.fetch_token(token_url='https://account.kkbox.com/oauth2/token', auth=auth)[
                                'access_token']

                except:
                       print('Opps, there\'s something wrong with your client_id or secret key. Please double check that it\'s correct.')


                #API call
                else:
                        endpoint = 'https://api.kkbox.com/v1.1/charts/{}?territory=TW'.format(tracklist_id)
                        headers = {"Authorization": "Bearer {}".format(token)}
                        response = requests.get(endpoint, headers=headers).json()
                        # print(response)

                        result = []
                        rank = 1
                        for item in response["tracks"]["data"]:
                                result.append([str(rank), item['album']['artist']['name'], item["album"]["name"],
                                               item["name"]])
                                rank += 1
                        header = ["Rank", "Artist Name", "Album Name", "Track Name"]

                        with open(fileName, 'w', newline='', encoding='utf-8-sig') as f:
                                w = csv.writer(f)
                                w.writerow(header)
                                w.writerows(result)
                        print('Done!')
