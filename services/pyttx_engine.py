import pyttsx3
import os

def generate_pyttsx(text, rate, filepath):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.save_to_file(text, filepath)
    engine.runAndWait()
