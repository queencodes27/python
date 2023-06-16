"""
Abstraction method :
process of handling complexity by hiding uncessary information from the user.     

"""


from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b
    
    def perimeter(self):
        return (self.a + self.b) * 2
    
    def __str__(self):
        return f"{self.a} {self.b}"
    
r = Rectangle(4, 5)
# print(r.area())

class Triangle(Shape):

    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        s = pow(p * (p - self.a) * (p - self.b) * (p - self.c), 1/2)
        return s
    
    def perimeter(self):
        return (self.a + self.b + self.c)
    
    def __str__(self):
        return f"{self.a} {self.b} {self.c}"
    
t = Triangle(3, 4, 5)
print(t.area())

class Circle(Shape):

    def __init__(self, r) -> None:
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2
    
    def perimeter(self):
        return 6.28 * self.r 
    
    def __str__(self):
        return f"{self.r}"
    


class Person:

    def __init__(self, full_name: str, age: int, gender: str, phone_number: str) -> None:
        self.full_name = full_name
        self.age = age
        self.gender = gender
        self.phone_number = phone_number

    
    def getInfo(self):
        return f"{self.full_name} {self.age} {self.gender} {self.phone_number}"
    

class Stundet(Person):

    def __init__(self, full_name: str, age: int, gender: str, phone_number: str, group: str) -> None:
        super().__init__(full_name, age, gender, phone_number)
        self.group = group

    def getInfo(self):
        return super().getInfo() + f"{self.group}"
    
    def getInfo(self, name):
        return f"{self.group} {name}"
    

s = Stundet('Ali Aliyev', 23, "Erkak", '+998901234567', '123')
# print(s.getInfo())



