import pyttsx3
import os
import uuid

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_audio(text, voice_id, rate):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")

    for v in voices:
        if voice_id.lower() in v.name.lower():
            engine.setProperty("voice", v.id)
            break

    engine.setProperty("rate", rate)

    filename = f"{uuid.uuid4()}.wav"
    path = os.path.join(OUTPUT_DIR, filename)

    engine.save_to_file(text, path)
    engine.runAndWait()

    return path
