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

4. Скачать файл libomp140.x86_64.dll и поместить его в 'C:\Windows\System32'
https://www.dllme.com/dll/files/libomp140_x86_64/00637fe34a6043031c9ae4c6cf0a891d/download

Для работы также понадобится установить ffmpeg:

Скачиваем релиз [отсюда](https://github.com/BtbN/FFmpeg-Builds/releases)

Из архивной папки bin все dll переносим в папку python, найти ее можно через команду

```
where python
```
