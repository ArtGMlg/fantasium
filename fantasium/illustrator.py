import json
import time
import requests


class Text2ImageAPI:

    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }
        self.base_prompts = [
            "Создай изображение, изображающее сцену из детской сказки с яркими цветами и абстрактными формами. Включи элементы, такие как волшебные существа. Изображение должно подходить к данному фрагменту сказки: "]

    def get_model(self):
        response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
        data = response.json()
        print(data)
        return data[0]['id']

    def generate(self, prompt, model, images=1, width=384, height=256):
        # Include previous prompts in the current prompt
        full_prompt = " ".join(self.base_prompts + [prompt])

        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {
                "name": "KANDINSKY",
                "query": f"{full_prompt}",
                "negativePromptUnclip": "старые мультфильмы, тусклость, СССР, мозаика"
            }
        }

        data = {
            'model_id': (None, model),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        return data['uuid']

    def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()
            if data['status'] == 'DONE':
                return data['images']

            attempts -= 1
            time.sleep(delay)
