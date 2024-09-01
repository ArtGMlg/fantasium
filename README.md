# fantasium

1. Создать окружение

   ```
   python -m venv .venv
   ```
2. Активировать

   ```
   ./.venv/Scripts/activate
   ```
3. Установить torch

   ```
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```
4. Установить зависимостb

   ```
      pip install -r requirements.txt
   ```


Для работы также понадобится установить ffmpeg:

Скачиваем релиз [отсюда](https://github.com/BtbN/FFmpeg-Builds/releases)

Из архивной папки bin все dll переносим в папку python, найти ее можно через команду

```
where python
```
Также для работы понадобится .env файл, в котором будут находится ключи для api, необхлдимые поля см. settings.py
