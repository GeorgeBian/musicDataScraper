from ytmusicapi import YTMusic
import csv

YTMusic.setup(filepath="headers_auth.json", headers_raw='''
accept: */*
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
authorization: SAPISIDHASH 1653625259_b53cc34bfe63dcbe2074720d4f4a8e901aebf819
content-length: 2051
content-type: application/json
cookie: VISITOR_INFO1_LIVE=rPbMrCin4So; PREF=tz=Asia.Shanghai&f5=30000&f6=1&f4=4000000; SID=Kgheebfr7Nj0vzO0d2YSsc6i1cWG9PLDRuI7Pyx_LdNOxLKzB-MA7OllFcGqKpNgzAkfIA.; __Secure-1PSID=Kgheebfr7Nj0vzO0d2YSsc6i1cWG9PLDRuI7Pyx_LdNOxLKzEjstiL6EoEm3gqXRfm9DKQ.; __Secure-3PSID=Kgheebfr7Nj0vzO0d2YSsc6i1cWG9PLDRuI7Pyx_LdNOxLKzpEUzIhK1spsNBSFweKPzOQ.; HSID=AHkRUwiI239SPfLBj; SSID=AugiTlZYl_fzk1SmV; APISID=AfZuvNSkO2iEtvnF/AenySMNoq0MfSZtvf; SAPISID=kH_bNd6pHHHQFah2/ALSqRbzjJq4SUCAv6; __Secure-1PAPISID=kH_bNd6pHHHQFah2/ALSqRbzjJq4SUCAv6; __Secure-3PAPISID=kH_bNd6pHHHQFah2/ALSqRbzjJq4SUCAv6; YSC=J55MTkkMGo4; LOGIN_INFO=AFmmF2swRAIgXrazYaTqW5q_uYZpAso3Tun17jYQRu30-K1DZn5QZ6QCIBMJoK0112gn-JgCnXwCdROGFTOZu7vn6OuJNJqFnXCN:QUQ3MjNmejhlVWRDUEFZSEJ6YmF0TVE0VDF2T200VldxZEpSNFJOTGZwUUFNY29LYmdMbTF1YTViazBRYTRzcXpLR2tlcEpXTFZIWUkyblNGWVJ4eFJET0U5eS1CdnJIVmplYlVrNy1tdGtQWlpfWm1feXVxRXdJRF80czZaVmNTTkptdElpMkxpVEFvOGYxaDJWZGZCUnRxZ1VQVlZibVNB; _gcl_au=1.1.1075268634.1653624744; SIDCC=AJi4QfHm5TxgVIT1v_jgSSNoxvlYeY3xga000THVddFQGwwcGNN9JOIjmoblgu2bzSbUnNCW4g; __Secure-3PSIDCC=AJi4QfEHjSvbA9eDg-SWMBD09KHeaiyvxNNieHjLlYkk4eRZAlNSbRjK2FoKDOR9fiNKZkVJfA
origin: https://music.youtube.com
referer: https://music.youtube.com/
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"
sec-ch-ua-arch: "x86"
sec-ch-ua-bitness: "64"
sec-ch-ua-full-version: "101.0.4951.64"
sec-ch-ua-full-version-list: " Not A;Brand";v="99.0.0.0", "Chromium";v="101.0.4951.64", "Google Chrome";v="101.0.4951.64"
sec-ch-ua-mobile: ?0
sec-ch-ua-model
sec-ch-ua-platform: "macOS"
sec-ch-ua-platform-version: "11.6.1"
sec-fetch-dest: empty
sec-fetch-mode: same-origin
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36
x-client-data: CIy2yQEIorbJAQjEtskBCKmdygEIwtnKAQiTocsBCNvvywEI54TMAQj/qswBCKSvzAEIiLDMAQi2sswBGKupygE=
Decoded:
message ClientVariations {
  // Active client experiment variation IDs.
  repeated int32 variation_id = [3300108, 3300130, 3300164, 3313321, 3321026, 3330195, 3340251, 3342951, 3347839, 3348388, 3348488, 3348790];
  // Active client experiment variation IDs that trigger server-side behavior.
  repeated int32 trigger_variation_id = [3314859];
}
x-goog-authuser: 0
x-goog-visitor-id: CgtyUGJNckNpbjRTbyiqo8GUBg%3D%3D
x-origin: https://music.youtube.com
x-youtube-client-name: 67
x-youtube-client-version: 1.20220525.01.00
''')
ytmusic = YTMusic('headers_auth.json')
#result = str(ytmusic.get_playlist(playlistId='RDCLAK5uy_mTDHYYJLCkFv8XL1Z8AFkMqF9RfQZzeRc')).replace('\'', '"')
tracks = ytmusic.get_playlist(playlistId='RDCLAK5uy_nZiG9ehz_MQoWQxY5yElsLHCcG0tv9PRg')['tracks']
result = []
rank = 1
for item in tracks:
    if item['album'] is None:
        result.append([str(rank), item['artists'][0]['name'], item["album"],
                   item["title"]])
    else:
        result.append([str(rank), item['artists'][0]['name'], item["album"]
        ['name'],
                       item["title"]])
    rank += 1
header = ["Rank", "Artist Name", "Album Name", "Track Name"]

with open('YT_request.csv', 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(result)
print('Done!')