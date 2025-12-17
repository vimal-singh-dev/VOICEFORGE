import pyttsx3
import os
import uuid

engine = pyttsx3.init()

def list_voices():
    voices = engine.getProperty("voices")
    return [
        {
            "id": v.id,
            "name": v.name,
            "language": v.languages
        }
        for v in voices
    ]

def generate_pyttsx(text, voice_id=None, rate=170):
    os.makedirs("output", exist_ok=True)

    filename = f"output/{uuid.uuid4()}.mp3"

    engine.setProperty("rate", rate)

    if voice_id:
        engine.setProperty("voice", voice_id)

    engine.save_to_file(text, filename)
    engine.runAndWait()

    return filename
