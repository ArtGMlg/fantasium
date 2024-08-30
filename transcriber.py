import whisper

class Transcriber:
  def __init__(self) -> None:
    self.model = whisper.load_model('base')
    pass
  
  def process(self, fileName: str):
    return self.model.transcribe(fileName, language='ru')['text']
