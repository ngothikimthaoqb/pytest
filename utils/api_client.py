# api_client.py
import requests
from utils import config

class APIClient:
    def __init__(self):
        self.base_url = config["baseUrl"]

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params)
        return response

    def post(self, endpoint, body=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=body)
        return response

    def put(self, endpoint, body=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, json=body)
        return response

    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url)
        return response
