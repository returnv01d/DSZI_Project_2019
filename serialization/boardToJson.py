import json


class boardToJson:
    def writeToJSON(list):
        with open('board.json', 'w') as outfile:
            json.dump(list, outfile)

