from module_config import *
from Master import *
import logging

class VA:
    def __init__(self, name):
        # Text-Speech engine config
        self.engine = pyttsx3.init('sapi5')
        self.engine.setProperty('voice', self.engine.getProperty('voices')[1].id)  
        self.name = name
        self.init = False
        self.master = None
        self.logger = self.set_logger()

        self.speak(self.greeting())

    def set_logger(self):
        logger = logging.getLogger("VA")
        logger.setLevel(logging.DEBUG)  # Set log level
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        file_handler = logging.FileHandler(f'{self.name}Logger.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger

    def greeting(self):
        import datetime
        hour = int(datetime.datetime.now().hour)
        if hour>= 0 and hour<12:
            s =  "Good Morning!"
    
        elif hour>= 12 and hour<18:
            s = "Good Afternoon!"   
    
        else:
            s = "Good Evening!"

        return s + f' I am {self.name}. At your service'
    
    # FUnction to take in text and convert to Audio
    def speak(self,text):
        self.engine.say(text)
        self.logger.debug(f'Saying : {text}')
        self.engine.runAndWait()
        
