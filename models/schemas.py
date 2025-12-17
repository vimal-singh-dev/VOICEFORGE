from pydantic import BaseModel

class TTSRequest(BaseModel):
    text: str
    engine: str = "pyttsx3"   # pyttsx3 | gtts
    rate: int = 170
    filename: str = "output"
