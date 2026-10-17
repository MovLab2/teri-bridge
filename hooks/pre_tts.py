import os
import tempfile

FLAG_PATH = os.path.join(tempfile.gettempdir(), "teri_avatar_ok.flag")

def pre_tts(event):
    if os.path.exists(FLAG_PATH):
        event.skip_tts = True
