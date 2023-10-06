from module_config import *

# Text-Speech engine config
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# FUnction to take in text and convert to Audio
def speak(text):
    engine.say(text)
    engine.runAndWait()

