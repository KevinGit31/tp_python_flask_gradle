import json
import os


def read_bd():
    data_base_file = os.path.join(os.path.dirname(__file__), 'bd.txt')
    file = open(data_base_file, "r")
    file_json = file.read()
    file.close()
    # y = json.dumps(file_json)
    # print(file_json)
    return file_json


# read_bd()
