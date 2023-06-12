"""
    HOME ASSIGMENTS
"""

from uuid import uuid4

class Apple:
    def __init__(self, device :str , produtc_year:int , model:str  ) -> None:
        self.device = device
        self.product_year = produtc_year
        self.model= model
        self.__Id = uuid4()
        self.model = model
        
    
    def getId(self):
        return self.__Id
    
    def get(self):
        return self.__kurs
    
    def addStorage(self, ):
        if kurs > 0:
            self.__kurs += kurs
    
    

s1 = Student("Ramazon", "Djamolov", "Sardor", 1) 
print(s1.getId())