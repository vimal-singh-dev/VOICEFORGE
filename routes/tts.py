from fastapi import APIRouter
from services.pyttsx_engine import generate_pyttsx, list_voices

router = APIRouter(prefix="/tts", tags=["Text-to-Speech"])

@router.get("/voices")
def get_voices():
    return list_voices()

@router.post("/convert")
def convert_text(
    text: str,
    voice_id: str | None = None,
    rate: int = 170
):
    file_path = generate_pyttsx(text, voice_id, rate)
    return {
        "status": "success",
        "audio_file": file_path
    }
