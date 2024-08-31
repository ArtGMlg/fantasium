import os
import torch
from tts_utils import apply_tts
from scipy.io.wavfile import write
from logmmse import logmmse
import numpy as np

class TtsModel:
    def __init__(self,):
        torch.set_grad_enabled(False)
        torch.set_num_threads(8)
        symbols = '_~абвгдеёжзийклмнопрстуфхцчшщъыьэюя +.,!?…:;–'

        if not os.path.isfile('model.jit'):
            torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v1_kseniya_16000.jit',
                                            'model.jit')

        self.model = torch.jit.load('model.jit',
                            map_location='cpu')
        self.model.eval()

    def get_audio(self, text):
        audio = apply_tts(texts=[text],
                        model=self.model,
                        sample_rate=8000,
                        symbols='_~абвгдеёжзийклмнопрстуфхцчшщъыьэюя +.,!?…:;–',
                        device='cpu')
        enhanced = logmmse(np.array(audio[0]), 16000, output_file=None, initial_noise=1, window_size=160, noise_threshold=0.15)
        filepath = 'filepath.wav'
        write(filepath, 16000, enhanced)

        return filepath
