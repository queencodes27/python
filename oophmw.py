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
    
    

# class Passenger:
#     def __init__(self, passportID: str, fullname: str, gender:str) -> None:
#         self.passportID = passportID
#         self.fullname = fullname
#         self.gender = gender
    
#     def getFull_Info(self):
#         return f"Passport id:{self.passportID} Full name:{self.fullname} Gender:{self.gender}"
    
#     def __str__(self) -> str:
#         return self.fullname

# passenger1 = Passenger("31195886", "Elon Musk", "male" )
# passenger2 = Passenger("81818109", "Bill Gates", "male")
# passenger3 = Passenger("9098708090", "Sardor M", "male")
# passengers = [passenger1, passenger2, passenger3]
# # print(passengers)

# class Driver:
#     def __init__(self, passportID: str, fullName: str, age: int) -> None:
#         self.passportID = passportID
#         self.fullName = fullName
#         self.age = age
        
#     def getFull_Info(self):
#         return self.fullName
    
#     def __str__(self) -> str:
#         return f"{self.passportID} {self.fullName} {self.age}"
    
# driver = Driver("AC777555", "Nadira Saip", 18)
# print(driver)
# print()

# class Train:
#     def __init__(self, trainID: str, name: str, speed: int, driver: Driver) -> None:
#         self.trainID = trainID
#         self.name = name
#         self.speed = speed
#         self.driver_obj = driver 
        
#     def setName(self):
#         self.name
    
#     def getFull_Info(self):
#         return f"{self.name}" 
    
#     def __str__(self) -> str:
#         return f" TRAIN_ID: {self.trainID}\n NAME: {self.name}\n SPEED: {self.speed}mph\n DRIVER: {self.driver_obj.getFull_Info()}\n\t "
    
# train = Train( "CTA-CHICAGO", "CTA-BlueLine", 70, driver ) 
# # print(train)  

# class Platform:
#     def __init__(self, platformID:str, status: bool) -> None:
#         self.platformID = platformID
#         self.status = status
    
#     def getFull_Info(self):
#         return f"{self.platformID} {self.status}" 
    
#     def __str__(self) -> str:
#         return f"{self.platformID} {self.status}"
    
# platform = Platform("CTA-1", True)
# print(platform)

# class Trip:
#     def __init__(self, start_from: str, to: str, train_obj:Train, platform_obj: Platform, passengers:list , priceTrip:int, dateTrip:str) -> None:
#         self.start_from = start_from
#         self.to = to
#         self.train_obj = train_obj
#         self.platform_obj = platform_obj
#         self.passengers_obj = passengers
#         self.priceTrip = priceTrip
#         self.dateTrip = dateTrip
     
#     def showData(self):
#         return self.train
    
#     def getFull_Info(self):
#         x = []
#         for i in self.passengers_obj:
#             x.append(str(i.getFull_Info())+" ")
#         y = ''.join(x)
#         return f" FROM:{self.start_from}\nEND:{self.to}\nTRAIN:{self.train_obj}\nPLATFORM:{self.platform_obj}\n PASSENGER:{y}\n PRICE:${self.priceTrip} DATE:{self.dateTrip}"
    
#     def toString(self):
#         return self.train_obj
        
#     # def addPassengers(self, passengers_obj: Passenger):
#     #     self.passengers.append(passengers_obj)
    
#     def __str__(self) -> str:
#         x = []
#         for i in self.passengers_obj:
#             x.append(str(i.getFull_Info())+" ")
#         y = ''.join(x)
#         return f" FROM: {self.start_from}\n END: {self.to}\n TRAIN: {self.train_obj}\n PLATFORM: {self.platform_obj} PASSENGERS: {y}\n PRICE: ${self.priceTrip} DATE: {self.dateTrip}"

# trip1 = Trip("Uzbekistan", "Switzerland", train, platform,[passenger1,passenger2, passenger3], 0,  "10/01/2023 - 11/01/2023" )
# trip2 = Trip("Switzerland", "Italy", train, platform,[passenger1, passenger2, passenger3], 0,  "11/01/2023 - 12/01/2023" )
# trip3 = Trip("Italy", "Greece", train, platform, [passenger1, passenger2, passenger3], 0, "12/01/2023 - 01/01/2024")
# trips = [trip1, trip2, trip3]
# # print(trip1.getFull_Info())


# class RailwayStation:
#     def __init__(self,name:str, address: str, trip: list) -> None:
#         self.name = name
#         self.address = address
#         self.trip = trip
        
#     def getFull_Info(self):
#         x = []
#         for i in self.trip:
#             x.append(str(i.getFull_Info())+" ")
#         z = ''.join(x) 
#         return f" NAME: {self.name}\n ADDRESS: {self.address}\n TRIP: {z}\n"
    
    
#     def __str__(self) -> str:
#         x = []
#         for i in self.trip:
#             x.append(str(i.getFull_Info())+" ")
#         z = ''.join(x) 
#         return f" NAME: {self.name}\n ADDRESS: {self.address}\n TRIP: {z}\n"
    
# railway = RailwayStation("Subway-USA", "5555 N Cumberland, Chicago, IL 60656", [trip1, trip2, trip3])

# print(railway) 


class Author:
    def __init__(self, first_name:str, last_name:str) -> None:
        self.first_name = first_name
        self.last_name = last_name
    
    def getFullname(self):
        return self.first_name + ' ' + self.last_name
    
    def __str__(self) -> None:
        return f"{self.first_name} {self.last_name}"

authors1 = Author("Michelle" ,"Obama")
authors2 = Author("Melinda" ,"Gates")
authors3 = Author("Maye", "Musk")
print(authors1.getFullname())

class Books:
    def __init__(self, name:str, pages:int, authors:Author) -> None:
        self.name = name
        self.pages = pages
        self.authors = []
    
    def getAuthors(self):
        x = []
        for i in self.authors:
            x.append(str(i.getAuthors()+ " "))
        y = " ".join(x)
        return f"  NAME: {self.name}\n PAGES: {self.pages}\n AUTHOR: {y}\n"
    
    def getName(self):
        return self.name
    
    def __str__(self) -> str:
        x = []
        for i in self.authors:
            x.append(str(i.getAuthors()+ " "))
        y = " ".join(x)
        
        return f" NAME: {self.name}\n PAGES: {self.pages}\n AUTHOR: {y}\n"        
book1 = Books("Becoming Michelle Obama",448, "Michelle Obama")
book2 = Books("Moment of Lift", 288, "Melinda Gates")
book3 = Books("A Woman Makes a Plan", 224, "Maye Musk")
x = [book1, book2, book3]
print(book1.getName)

            
        


        
    
    