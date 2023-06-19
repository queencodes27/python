

# """
# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.

"""
@property: pythonic way to use getter and setter methods.
in order to use for private methods you can call

Getter: A method that allows you to access an attribute in 
a given class. 
Setter: A method that allows you to set 
or mutate the value of an attribute in a class.

"""

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
# class Vehicle:
#     def __init__(self, model:str,  speed:int, year:int):
#         self.model = model
#         self.speed = speed
#         self.year = year

#     def getStart(self):
#         return self.model

#     def __str__(self): # magic method
#         return self.model

# class Car(Vehicle):
#     def __init__(self, model:str,  speed:int, year:int, price: int, milage:int) -> None:
#         super().__init__( model,  speed, year)
#         self.price = price
#         self.milage = milage
        
# class Motorcycle(Vehicle):
#     def __init__(self, model:str,  speed:int, year:int, brand:str) -> None:
#         super().__init__(model, speed, year)
#         self.type = type
#         self.brand = brand
    
    
# car = Vehicle("Rolls Royce", 100, 2020)
# print(car)

# bike = Motorcycle("XYZ", 100, 2023, "Harley Davidson")
# print(bike)


# class Phone:
#     def __init__(self, name:str,  color:str, price:float):
#         self.name = name
#         self.color= color
#         self.price = price

#     def setName(self, name):
#         self.name = name
    
#     def getName(self):
#         return self.name
    
#     def getColor(self):
#         return self.color
    
#     def getColor(self):
#         return self.color
    
#     def setPrice(self, price):
#         self.price = price
    
#     def getPrice(self):
#         return self.price 
    
#     def getInfo(self):
#         return self.info
    
#     def __str__(self): # magic method
#         return f"{self.name} {self.color} {self.price}"
    
# phone1 = Phone("Redme Note4x", "black", 150)
# print(phone1)
# phone2 = Phone("IphoneX", "white", 700)
# print(phone2)




# class Car:
#     def __init__(self, name:str, color:str, speed:int):
#         self.name = name
#         self.speed = speed
#         self.color = color

#     def __str__(self): # magic method
#         return f"{self.name} {self.color} {self.speed}"
    
# car1 = Car("Lacetti", " white", 220)
# print(car1)
# car2 = Car("Malibu", "black", 260)
# print(car2)
# car3 = Car("Matiz", "grey", 180)


"""
ENCAPSULATION
    
"""
import datetime

# class User:
#     __user_id = 777

#     def __init__(self, username: str, full_name: str, age: int, email: str) -> None:
#         self.username = username
#         self.full_name = full_name
#         self.__age = age
#         self._email = email

#     def getYaer(self):
#         return datetime.datetime.now().year - self.__age
    
#     def getAge(self):
#         return self.__age

#     def __str__(self) -> str:
#         return self.username
    
# user = User('root', 'Toshmat Karimov', 20, 'toshmat@gmail.com')

# print(user.getYaer())
# print(user.getAge())
# print(user._email)

# class Admin(User):

#     def __init__(self, username: str, full_name: str, age: int, email: str, is_admin: bool) -> None:
#         super().__init__(username, full_name, age, email)
#         self.__is_admin = is_admin

#     def getIs_admin(self):
#         return self.__is_admin
    
#     def __str__(self):
#         return f"{self.full_name} {self.getAge()} {self._email} {self.__is_admin}"
    

# admin = Admin('admin', 'Ali Aliyev', 33, 'admin@gmail.com', True)

# print(admin)


# class Student:

#     def __init__(self, s_id: int, full_name: str, age: int) -> None:
#         self.s_id = s_id
#         self.full_name = full_name
#         self.age = age

    
#     def __str__(self):
#         return self.full_name
    

# s1 = Student(123, 'Ali Aliyev', 23)
# s2 = Student(124, "Toshmat Karimov", 24)
# s3 = Student(125, 'Aziz Azizov', 21)

# class Group:

#     def __init__(self, name: str) -> None:
#         self.name = name
#         self.students = []

#     def addStudent(self, student_obj: Student):
#         self.students.append(student_obj)

#     def getStudents(self):
#         return self.students

#     def __str__(self) -> str:
#         my_text = f"Group name: {self.name}\n\t"
#         for index, student in enumerate(self.students, 1):
#             my_text += f"{index} {student}\n\t"
#         return my_text
    
# group1 = Group('FSP U-3/23',)
# group1.addStudent(s1)
# group1.addStudent(s2)
# group1.addStudent(s3)
# print(group1)
# print(group1.getStudents())

"""
ENCAPSULATION CLASS
"""
class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
point1 = Point(3, 5)
point2 = Point(-5, 4)

class Circle:

    def __init__(self, raduis: int, color: str, point: Point):
        self.raduis  = raduis
        self.color = color
        self.p_obj = point

    def __str__(self):
        return f"Raduis: {self.raduis}\nColor: {self.color}\nPoint: {self.p_obj}\n"
    
c = Circle(5, 'yellow', point1)
print(c)


class Rectangle:

    def __init__(self, point1: Point, point2: Point, color: str) -> None:
        self.color = color
        print(self.checkPoints(point1, point2))
        if self.checkPoints(point1, point2):
            self.point1 = point1
            self.point2 = point2
        else:
            print(f"{point1} va {point2} nuqtalardan Rectangle yasab bo'lmaydi !!!")
        

    
    @staticmethod
    def checkPoints(p1: Point, p2: Point):
        return p1.x != p2.x and p1.y != p2.y
    
    def __str__(self):
        return f"{self.point1} {self.point2}"
    

r = Rectangle(point1, point2, 'red')
print(r)


