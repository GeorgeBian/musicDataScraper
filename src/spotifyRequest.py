import json

from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
import requests
from jsonConverter import jsonConverter

class spotifyRequest:
        def __init__(self, client_id=r'01071569859f4de890de539ad1ca14ee', client_secret=r'02561150200d4071a743ab6e0d3d5db0'):
                self.client_id = client_id
                self.client_secret = client_secret
        def request(self, fileName):
                #Authentication with oAuth2 to retreive token for API call
                try:
                        auth = HTTPBasicAuth(self.client_id, self.client_secret)
                        client = BackendApplicationClient(client_id=self.client_id)
                        oauth = OAuth2Session(client=client)
                        token = oauth.fetch_token(token_url='https://accounts.spotify.com/api/token', auth=auth)['access_token']
                except:
                       print('Opps, there\'s something wrong with your client_id or secret key. Please double check that it\'s correct.')


                #API call
                else:
                        endpoint = 'https://api.spotify.com/v1/playlists/37i9dQZF1DX387yApX7ZA5'
                        headers = {"Authorization": "Bearer {}".format(token)}
                        response = requests.get(endpoint, headers=headers).json()
                        converter = jsonConverter(fileName)
                        converter.convert(response)

                # #Output to a json file
                # with open(fileName, 'w') as json_file:
                #         json.dump(response, json_file, indent=6, ensure_ascii=False)






