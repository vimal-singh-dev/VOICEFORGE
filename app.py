from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from tts import text_to_speech
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.post("/convert")
def convert(text: str = Form(...)):
    audio_path = text_to_speech(text)
    return FileResponse(audio_path, media_type="audio/mpeg", filename="speech.mp3")
