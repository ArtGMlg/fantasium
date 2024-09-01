import os
import torch
import base64

class TtsModel:
    def __init__(self,):
        torch.set_grad_enabled(False)
        torch.set_num_threads(12)

        if not os.path.isfile('model.pt'):
            torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v4_ru.pt',
                                        'model.pt')  

        self.model = torch.package.PackageImporter('model.pt').load_pickle("tts_models", "model")
        self.model.to('cpu')

    def get_audio(self, text):
        audio_path = self.model.save_wav(text=text,
                             speaker='xenia',
                             sample_rate=8000)
        with open(audio_path, "rb") as f:
            audio_data = base64.b64encode(f.read())

        return audio_data
