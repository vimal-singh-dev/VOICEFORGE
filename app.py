from fastapi import FastAPI
from routes.tts import router as tts_router

app = FastAPI(title="VoiceForge v2")

app.include_router(tts_router, prefix="/tts")

@app.get("/")
def home():
    return {"status": "VoiceForge v2 running"}
