import time
import uuid
import requests

ACCESS_TOKEN = None
TOKEN_LIFE_TIME: float = 0


def get_access_token():
    global ACCESS_TOKEN, TOKEN_LIFE_TIME
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    payload = 'scope=GIGACHAT_API_CORP'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': str(uuid.uuid4()),
        'Authorization': 'Basic Yjg4MTQzMmUtNDAwMS00NDk0LThjOGUtNmU5ZWQ2YzQ4NDQ2OjcxODg0YjhmLTYyMDItNDQ5ZC04NjI2LTY1NjM0ZjU1MGJlYg=='
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    response_data = response.json()

    ACCESS_TOKEN = response_data['access_token']
    TOKEN_LIFE_TIME = response.json()["expires_at"]


def get_token():
    global ACCESS_TOKEN, TOKEN_LIFE_TIME
    if ACCESS_TOKEN is None or time.time() >= TOKEN_LIFE_TIME:
        get_access_token()
