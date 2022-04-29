import csv
import json

class jsonConverter:
    def __init__(self, outputName):
        self.outputName = outputName
    def convert(self, response):
        # f = open(file)
        # x = json.load(f)
        rank = 1
        result = []
        for item in response["tracks"]["items"]:
            result.append([str(rank), item["track"]["artists"][0]["name"], item["track"]["album"]["name"], item["track"]["name"]])
            rank += 1
        # f.close()

        header = ["Rank", "Artist Name", "Album Name", "Track Name"]

        with open(self.outputName, 'w', newline='', encoding='utf-8-sig') as f:
            w = csv.writer(f)
            w.writerow(header)
            w.writerows(result)
        print('Done!')

