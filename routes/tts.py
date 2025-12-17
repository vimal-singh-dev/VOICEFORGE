from fastapi import APIRouter
from models.schemas import TTSRequest
from services.pyttsx_engine import generate_pyttsx
from services.gtts_engine import generate_gtts
from utils.file_manager import get_path

router = APIRouter(prefix="/tts", tags=["TTS"])

@router.post("/convert")
def convert(req: TTSRequest):
    if req.engine == "gtts":
        path = get_path(req.filename, "mp3")
        generate_gtts(req.text, path)
    else:
        path = get_path(req.filename, "wav")
        generate_pyttsx(req.text, req.rate, path)

    return {
        "status": "success",
        "engine": req.engine,
        "file": path
    }
