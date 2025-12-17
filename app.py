from fastapi import FastAPI
from routes.tts import router as tts_router

app = FastAPI(title="VoiceForge v3")

app.include_router(tts_router)

@app.get("/")
def root():
    return {"status": "VoiceForge v3 running"}
