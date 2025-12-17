import os

OUTPUT_DIR = "outputs/audio"

def ensure_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_path(filename, ext):
    ensure_dir()
    return f"{OUTPUT_DIR}/{filename}.{ext}"
