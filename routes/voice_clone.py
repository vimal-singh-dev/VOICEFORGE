from fastapi import APIRouter, UploadFile, File, Form
from services.voice_encoder import save_reference_audio
from services.voice_cloner import clone_voice

router = APIRouter(prefix="/clone", tags=["Voice Cloning"])

@router.post("/")
async def clone(
    text: str = Form(...),
    voice: UploadFile = File(...)
):
    ref_path = save_reference_audio(voice)
    output = clone_voice(text, ref_path)

    return {
        "status": "success",
        "output_audio": output
    }
