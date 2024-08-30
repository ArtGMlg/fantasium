import base64
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from models.illustrator_prompt import IllBody
from pydantic import BaseModel
from illustrator import Text2ImageAPI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

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
    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', 'F847186AE65345C881E17DA1677DDE20', '454F6AFF45FCD99661D322872774111E')
    model_id = api.get_model()
    uuid = api.generate(model.sentence, model_id)
    images = api.check_generation(uuid)
    image_data = base64.b64decode(images[0])
    with open('output_image.jpg', 'wb') as image_file:
        image_file.write(image_data)

    print("Image saved as output_image.jpg")
    return ''