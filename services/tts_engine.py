import pyttsx3
import uuid

engine = pyttsx3.init()

def get_voices():
    voices = engine.getProperty("voices")
    return [
        {
            "id": v.id,
            "name": v.name,
            "lang": v.languages
        }
        for v in voices
    ]

def synthesize(text: str, voice_id: str = None):
    if voice_id:
        engine.setProperty("voice", voice_id)

    filename = f"audio_{uuid.uuid4().hex}.wav"
    engine.save_to_file(text, filename)
    engine.runAndWait()

    return filename
