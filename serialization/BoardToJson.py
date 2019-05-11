import json


class BoardToJson:
    def __init__(self):
        self.a = 0
    def writeToJSON(self, list):
        with open('board.json', 'w') as outfile:
            json.dump(list, outfile, default=lambda x: x.__dict__)

