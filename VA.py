from module_config import *
from Master import *

class VA:
    def __init__(self, name):
        # Text-Speech engine config
        self.engine = pyttsx3.init('sapi5')
        self.engine.setProperty('voice', self.engine.getProperty('voices')[1].id)  
        self.name = name
        self.init = False
        self.master = None
        self.speak(self.greeting())

    def greeting(self):
        import datetime
        hour = int(datetime.datetime.now().hour)
        if hour>= 0 and hour<12:
            s =  "Good Morning"
    
        elif hour>= 12 and hour<18:
            s = "Good Afternoon"   
    
        else:
            s = "Good Evening"

        return s + f'I am {self.name}. At your service'
    
# FUnction to take in text and convert to Audio
def speak(self,text):
    self.engine.say(text)
    self.engine.runAndWait()
    
