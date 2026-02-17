import requests
import logging

logging.basicConfig(level=logging.INFO)


class ApiClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {"User-Agent": "Mozilla/5.0"}

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        logging.info(f"GET request to {url}")
        response = requests.get(url, headers=self.headers)
        logging.info(f"Response status: {response.status_code}")
        return response

    def post(self, endpoint, data):
        url = f"{self.base_url}{endpoint}"
        logging.info(f"POST request to {url}")
        response = requests.post(url, json=data, headers=self.headers)
        logging.info(f"Response status: {response.status_code}")
        return response




