import json


def read_json(DATA_FILE):
    with open(DATA_FILE, 'r') as file:
        return json.load(file)


def write_json(DATE_FILE, data):
    with open(DATE_FILE, 'w') as file:
        json.dump(data, file, indent=4)
