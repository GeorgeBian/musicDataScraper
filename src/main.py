from jsonConverter import jsonConverter
from spotifyRequest import spotifyRequest
from KKBOXrequest import KKBOXrequest

if __name__ == '__main__':
    url = (input("Please give me the url to the tracklist/playlist: ") or 'https://open.spotify.com/playlist/37i9dQZF1DX387yApX7ZA5?si=44166f1431c14104&nd=1')

    website_split = url.split('.')
    request_website = ''
    try:
        if 'spotify' in website_split:
            request_website = 'spotify'
        elif 'apple' in website_split:
            request_website = 'apple'
        elif 'kkbox' in website_split:
            request_website = 'kkbox'
        else:
            raise NameError
    except NameError:
        print('Please enter a valid website url. Supported websites are: spotify.com, apple.com, and kkbox.com')
        raise

    print('The website you reqeusted is: ' + request_website)
    client_id = (input('Please input your client_id: ') or '01071569859f4de890de539ad1ca14ee')
    client_secret = (input('Please input your client_secret: ') or '02561150200d4071a743ab6e0d3d5db0')
    fileName = (input('(Optional) Tell me what I should name the output file. ' +
                      'Default filename will be: \"request.csv\" \n') or 'request.csv')
    print('Thanks. Processing your request... \n')

    if request_website == 'spotify':
        tracklist_id = url.split('/')[-1]
        curr_request = spotifyRequest(client_id, client_secret)
        curr_request.request(tracklist_id, fileName)

    elif request_website == 'kkbox':
        tracklist_id = url.split('/')[-1]
        curr_request = KKBOXrequest(client_id, client_secret)
        curr_request.request(tracklist_id, fileName)



