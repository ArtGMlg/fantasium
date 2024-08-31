import datetime
import uuid
import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), 'envs/key.env')
load_dotenv(dotenv_path)
KEY = os.environ.get('KEY')

class Tokener:
    def __init__(self,):
        self.token = None
        self.token_end_time = None

    def get_access_token(self,):
        url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
        payload = 'scope=GIGACHAT_API_CORP'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'RqUID': str(uuid.uuid4()),
            'Authorization': f'Basic {KEY}'
        }

        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        response_data = response.json()

        self.token = response_data['access_token']
        self.token_end_time = datetime.datetime.fromtimestamp(response.json()["expires_at"]/1000)

    def get_token(self,):
        if self.token == None or datetime.datetime.now() >= self.token_end_time:
            self.get_access_token()
        return self.token
