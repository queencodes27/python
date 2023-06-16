"""
    HOME ASSIGMENTS
"""
"""

ENCAPSULATION
"""
    

# class Apple:
#     def __init__(self, device :str , produtc_year:int , model:str, price ) -> None:
#         self.device = device
#         self.product_year = produtc_year
#         self.model= model
#         self._price = price
    
#     def getFullinfo(self):
#         return f"{self.device} {self.product_year} {self.model} {self._price}$"
    
#     def __str__(self):
#         return self.getFullinfo()
    
# class Macbookpro(Apple):
#     def __init__(self, device: str, produtc_year: int, model: str, price, icore) -> None:
#         super().__init__(device, produtc_year, model, price)
#         self.__icore = icore
        
    
#     def getFullinfo(self):
#         return f"{self.device} {self.product_year} {self.model} {self._price}$ {self.__icore}"
        
        
#     def __str__(self):
#         return self.device

# class Ipadpro(Apple):
#     def __init__(self, device: str, produtc_year: int, model: str, price, inch) -> None:
#         super().__init__(device, produtc_year, model, price)
#         self.__inch = inch
    
#     def getFullinfo(self):
#         return f"{self.device} {self.product_year} {self.model} {self.__price}$ {self.icore} {self.inch}"
            
    
#     def __str__(self):
#         return super().getFullinfo()
    
# class Airpods(Ipadpro):
#     def __init__(self, device: str, produtc_year: int, model: str, price) -> None:
#         super().__init__(device, produtc_year, model, price)
        
#     def getFullinfo(self):
#         return super().getFullinfo()
    
#     def get__str__(self):
#         return super().getFullinfo()
    
# mac = Apple("MacBookAir", 2023,"air", 999 )
# print(mac.getFullinfo())

# macbookpro = Macbookpro("macbookpro", 2023, "pro", 2000, 16)
# print(macbookpro.getFullinfo())

# ipad = Ipadpro("ipadpro", 2023, "pro", 1000, 12.9)
# print(ipad.getFullinfo())

# pod = Airpods("Airpods", 2023, "airpods", 199)
# print(pod.getFullinfo())


# class Point:
#     def __init__(self, coordinatex:int, coordinatey:int) -> None:
#         self.coordinatex = coordinatex
#         self.coordinatey = coordinatey
        
#     def __str__(self) -> str:
#         return f"{self.coordinatex} {self.coordinatey}"

# point1 = Point(2, 7)
# point2 = Point(1, -9)

# class Circle:
#     def __init__(self, radius: int, color:str, point_obj: Point) -> None:
#         self.radius = radius
#         self.color = color
#         self.p_obj = point_obj 
        
    
#     def __str__(self):
#         return f"{self.radius} {self.color} {self.p_obj} "

# circle = Circle(5, "white", point1)
# print(circle)
        
# class Rectange:
#     def __init__(self, color: str, point1_obj: Point, point2_obj: Point) -> None:
#         self.color = color
#         if self.checkPoints(point1, point2):
#             self.point1 = point1
#             self.point2 = point2
#         else:
#             print (f"{point1} and {point2} is not rectange")
        
#     @staticmethod    
#     def checkPoints(point1, point2):
#         return point1.coordinatex != point2.coordinatey and point1.coordinatey != point2.coordinatey
    
#     def __str__(self) -> str:
#         return f"{self.point1} {self.point2}"

# r = Rectange("black", point1, point2)
# print(r)
        
        