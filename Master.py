class Master:
    def __init__(self, name:str, age:int, male:bool) -> None:
        self.name = name
        self.age = age
        self.male = male
        self.info = {}

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_gender(self, text:bool = False):
        if text:
            return "Male" if self.male else "Female"
        else:
            return self.male
    
    def get_info(self, key:str):
            return self.info.get(key)
    
    def add_info(self,key:str,info):
         self.info[key] = info