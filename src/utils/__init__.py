import json
import os
import requests

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, "../configs/production.json"), "r") as f:
    config = json.load(f)
    # print(config.json())

def get(endpoint, params=None):
        basleUrl= config["baseUrl"]
        url = f"{basleUrl}{endpoint}"
        response = requests.get(url, params=params)
        return response
