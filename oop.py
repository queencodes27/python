

# """
# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.

# 1. ABSTRACTION
# 2. ENCAPSULATION
# 3. INHERITANCE
# 4. POLYMORPHISM



# """

# """
# The self Parameter
# The self parameter is a reference to the current 
# instance of the class, and is used to access variables that belongs to the class.

# It does not have to be named self , you can call 
# it whatever you like, but it has to be the first parameter of any function in the class:
# """
# """

# The built-in __init__() function:to assign values to object properties when class is being initiated
# """
# # class Person:
# #  def __init__(self, name, age):
# #     self.name = name
# #     self.age = age

# # p1 = Person("John", 36)

# # print(p1.name)
# # print(p1.age)
# """
# The __str__() function : controls what should be returned when the class object is represented as a string
# """
# # class Person:
# #   def __init__(self, name, age):
# #     self.name = name
# #     self.age = age

# #   def __str__(self):
# #     return f"{self.name}({self.age})"

# # p1 = Person("John", 36)

# # print(p1)

# class Phone:
#     def __init__(self, name:str, price:int, color:str):
#         self.name = name
#         self.color = color
#         self.price = price

#     def getName(self):
#         return self.name 
    
#     def getPrice(self):
#         return self.price
    
#     def getColor(self):
#         return self.color
    
#     def __str__(self): # magic method
#         return self.name
        
    
# phone1 = Phone("Iphone", 100000, "pink")
# phone2 = Phone("samsung", 20000, "white")
# phone3 = Phone("Nokia", 5000, "black")

# phones = [phone1,phone2,phone3]
# print(phone1.getColor(),phone2.getName(), phone3.getPrice())

# s = 0
# for obj in phones:
#     if obj.getColor() == "black":
#         s += obj.getPrice()
# print(s)

"""
INHERITANCE 

"""
class Vehicle:
    def __init__(self, model:str,  speed:int, year:int):
        self.model = model
        self.speed = speed
        self.year = year

    def getStart(self):
        return self.model

    def __str__(self): # magic method
        return self.model

class Car(Vehicle):
    def __init__(self, model:str,  speed:int, year:int, price: int, milage:int) -> None:
        super().__init__( model,  speed, year)
        self.price = price
        self.milage = milage
        
class Motorcycle(Vehicle):
    def __init__(self, model:str,  speed:int, year:int, brand:str) -> None:
        super().__init__(model, speed, year)
        self.type = type
        self.brand = brand
    
    
car = Vehicle("Rolls Royce", 100, 2020)
print(car)

bike = Motorcycle("XYZ", 100, 2023, "Harley Davidson")
print(bike)


