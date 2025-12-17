from fastapi import APIRouter
from services.tts_engine import get_voices, synthesize

router = APIRouter()

@router.get("/voices")
def voices():
    return get_voices()

@router.post("/speak")
def speak(text: str, voice_id: str = None):
    file = synthesize(text, voice_id)
    return {"audio_file": file}
