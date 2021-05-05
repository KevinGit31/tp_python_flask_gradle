import json


def read_bd():
    file = open("bd.txt", "r")
    file_json = file.read()
    # y = json.dumps(file_json)
    print(file_json)
    return file_json


# read_bd()
