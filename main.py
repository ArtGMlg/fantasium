import base64
import json
import requests
import numpy as np
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from chat_tokener import Tokener
from models.schemas import IllBody, Message
from illustrator import Text2ImageAPI
from transcriber import Transcriber

app = FastAPI()
tokener = Tokener()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

t = Transcriber()

conversation_histories = {}

# Redirect / -> Swagger-UI documentation
@app.get("/")
def main_function():
    """
    # Redirect
    to documentation (`/docs/`).
    """
    return RedirectResponse(url="/docs/")


@app.post("/illustrator")
async def send_illustator(model: IllBody):
    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', 'F847186AE65345C881E17DA1677DDE20',
                        '454F6AFF45FCD99661D322872774111E')
    model_id = api.get_model()
    uuid = api.generate(model.sentence, model_id)
    images = api.check_generation(uuid)
    image_data = base64.b64decode(images[0])
    with open('output_image.jpg', 'wb') as image_file:
        image_file.write(image_data)

    print("Image saved as output_image.jpg")
    return ''


@app.post('/transcribe')
async def upload_file(file: UploadFile = File()):
    context = await file.read()

    with open('temp_file.wav', 'wb') as temp_file:
        temp_file.write(context)

    result = t.process('temp_file.wav')

    return {"transcription": result}


@app.post("/generate_story")
async def generate_story(message: Message):
    token = tokener.get_token()

    if message.chat_id not in conversation_histories:
        conversation_histories[message.chat_id] = [
            {
                "role": "system",
                "content": "Ты писатель книжек для детей. Тебе нужно сочинить сказку во время интерактивного общения с пользователем. Помни, что пользователь - ребенок, и он общается проще, чем взрослый, поэтому твоя задача сочинить понятную для него сказку. Также отвечай небольшими предложениями, чтобы ребенок мог продолжить твою сказку самостоятельно, а направив тебе ответ, получил еще предложение от тебя, так, пока ты не закончишь, но помни, сказка не должна утомить ребенка, поэтому должна быть достаточно короткой. Также не забывай, что один раз определив героев сказки, ты не можешь заменять их, а только добавлять новых."
            }
        ]

    user_message = {
        "role": "user",
        "content": f"{message.message}"
        }

    conversation_histories[message.chat_id].append(user_message)

    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
    payload = json.dumps({
        "model": "GigaChat",
        "messages": conversation_histories[message.chat_id],
        "n": 1,
        "stream": False,
        "update_interval": 0
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    story_content = response.json()['choices'][0]['message']['content']

    conversation_histories[message.chat_id].append({
        "role": "assistant",
        "content": story_content
    })

    return {"story": story_content}
