from fastapi import APIRouter, Form, UploadFile, File
from fastapi.responses import FileResponse, HTMLResponse
from services.pyttsx_engine import generate_audio
from fastapi.templating import Jinja2Templates
from fastapi import Request

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/ui", response_class=HTMLResponse)
def ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/convert")
async def convert(
    text: str = Form(...),
    voice: str = Form(...),
    rate: int = Form(150),
    pitch: int = Form(50),
    voice_file: UploadFile = File(None)
):
    output_path = generate_audio(text, voice, rate)
    return FileResponse(output_path, media_type="audio/wav", filename="voiceforge.wav")
