from fastapi import FastAPI
from routes.tts import router

app = FastAPI(title="VoiceForge v3")

app.include_router(router)

@app.get("/")
def root():
    return {"status": "VoiceForge v3 running"}
