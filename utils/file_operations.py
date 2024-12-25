import json


def read_json(DATA_FILE):
    with open(DATA_FILE, 'r') as file:
        return json.load(file)
