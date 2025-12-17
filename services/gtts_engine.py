from gtts import gTTS

def generate_gtts(text, filepath):
    tts = gTTS(text=text, lang='en')
    tts.save(filepath)
