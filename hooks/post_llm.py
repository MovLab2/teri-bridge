import subprocess
import requests
import os
import tempfile

FLAG_PATH = os.path.join(tempfile.gettempdir(), "teri_avatar_ok.flag")

def post_llm(event):
    text = (event.response or "").strip()
    if not text:
        return
    try:
        ip = subprocess.check_output(
            ["wsl", "hostname", "-I"],
            timeout=3, stderr=subprocess.DEVNULL
        ).decode().strip().split()[0]
    except Exception:
        if os.path.exists(FLAG_PATH):
            os.remove(FLAG_PATH)
        return
    try:
        requests.post(f"http://{ip}:5013/say", json={"text": text}, timeout=2)
        with open(FLAG_PATH, "w") as f:
            f.write("ok")
    except Exception:
        if os.path.exists(FLAG_PATH):
            os.remove(FLAG_PATH)
