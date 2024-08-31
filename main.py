import json
import requests
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
import base64

from text_to_speech import TtsModel
from chat_tokener import Tokener
from models.schemas import Message
from illustrator import Text2ImageAPI
from transcriber import Transcriber

app = FastAPI()
tokener = Tokener()
ttsmodel = TtsModel()
transcribe = Transcriber()
#TODO выкинуть в .env
api = Text2ImageAPI('https://api-key.fusionbrain.ai/', 'F847186AE65345C881E17DA1677DDE20', '454F6AFF45FCD99661D322872774111E')
model_id = api.get_model()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)
conversation_histories = {}

# Redirect / -> Swagger-UI documentation
@app.get("/")
def main_function():
    """
    # Redirect
    to documentation (`/docs/`).
    """
    return RedirectResponse(url="/docs/")

@app.post("/generate_complete")
def generate_complete(message: Message):
    token = tokener.get_token()
    if message.chat_id not in conversation_histories:
        conversation_histories[message.chat_id] = [
            {
                "role": "system",
                "content": "Ты писатель книжек для детей. Тебе нужно сочинить сказку во время интерактивного общения с пользователем. Помни, что пользователь - ребенок, и он общается проще, чем взрослый, поэтому твоя задача сочинить понятную для него сказку. Также отвечай небольшими предложениями, чтобы ребенок мог продолжить твою сказку самостоятельно."
            }
        ]

    user_message = {
        "role": "user",
        "content": message.message
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

    response = requests.post(url, headers=headers, data=payload, verify=False)
    story_content = response.json()['choices'][0]['message']['content']
    conversation_histories[message.chat_id].append({
        "role": "assistant",
        "content": story_content
    })

    filepath = ttsmodel.get_audio(story_content)
    with open(filepath, "rb") as f:
       audio_data = base64.b64encode(f.read())

    return {
        "story": story_content,
        "transcription": audio_data,
    }

@app.post("/illustrator")
async def send_illustator(model: Message):
    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', 'F847186AE65345C881E17DA1677DDE20',
                        '454F6AFF45FCD99661D322872774111E')
    model_id = api.get_model()
    uuid = api.generate(model.sentence, model_id)
    images = api.check_generation(uuid)

    return {"image": images[0]}


@app.post('/transcribe')
async def upload_file(file: UploadFile = File()):
    context = await file.read()

    with open('temp_file.wav', 'wb') as temp_file:
        temp_file.write(context)
        result = transcribe.process('temp_file.wav')

    return {"transcription": result}
