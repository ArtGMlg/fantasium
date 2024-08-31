from pydantic import BaseModel
class IllBody(BaseModel):
    sentence: str

class Message(BaseModel):
    message: str
    chat_id: str