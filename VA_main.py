from VA import *
from pickle import Pickler, Unpickler
import speech_recognition as sr
from time import time
import logging 
import threading
# Backlog to track unsaved changes
BackLog = []

# Logger for LISTENER
logger01 = logging.getLogger('listener')
logger01.setLevel(logging.DEBUG)  # Set log level
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_handler = logging.FileHandler('ListenerLogger.log')
file_handler.setFormatter(formatter)
logger01.addHandler(file_handler)

# Logger for VA
logger02 = logging.getLogger('Assistant')
logger02.setLevel(logging.WARNING)  # Set log level
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_handler = logging.FileHandler('AssistantLogger.log')
file_handler.setFormatter(formatter)
logger02.addHandler(file_handler)

# Logger for Serialization
logger03 = logging.getLogger('Serialization')
logger03.setLevel(logging.WARNING)  # Set log level
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_handler = logging.FileHandler('SerializationLogger.log')
file_handler.setFormatter(formatter)
logger03.addHandler(file_handler)

r = sr.Recognizer()
# Listens for user inputs
def listen():
    
    with sr.Microphone() as source:
         
        logger01.debug("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        logger01.debug("Recognizing...")    
        query = r.recognize_google(audio, language ='en-in')
        logger01.debug(f"User said: {query}")
  
    except Exception as e:
        logger01.warning(f'Error {e}')    
        print(f"Unable to Recognize your voice. {e}")  
        return "None"
     
    return query

# checks for a word within a reply
def check_for(reply: str, search:str) -> bool: 
    words = reply.split()
    for word in words:
        if word.lower() == search.lower():
            return True
    else:
        return False

if __name__ == "__main__":
    while True:
        print("Say hello followed by Virtual Assitant's name")
        reply = listen()
        words = reply.split()
        for word in words:
            if word.lower() != "hello":
                name = word
                break
        print(f"Your Assistant's name is {name.title()}. Is this correct?")
        command = listen()
        if check_for(command, "yes"):
            jarvis = VA(name.title())
            break
        else:
            continue