 """1 ex boshqich shart operator """

a = int(input("write a number:"))
b = int(input("write a number:"))
D = a ** 2 + b ** 2
C = (a + b) ** 2
if D > C:
     print("sum of power of 2 is bigger")
else :
     print("the sum of squares of bigger")

"""2 ex""""

# a = int(input("uchburchakni tomonini kiriting: "))
# b = int(input("uchburchakni tomonini kiriting: "))
# c = int(input("uchburchakni tomonini kiriting: "))

# if a == b != c:
#     print("uchburchak tengyonli: ")
# else:
#     print("uchburchak tengyonli emas")

"""3 ex"""

# year = (int(input("yil kiriting: "))) #kabisa yili manfiy kiritiladi!

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     if 0 < year < 2000:
#      print(f"{year} yil eramizdagi – kabisa yili")
#     elif year < 0:
#        print(f"{year} yil eramizdan avvalgi – kabisa yili")
# else:
#     print(f"{year} kabisa yili emas")

"""4 Ex"""

# harid = int(input('harid qiymatini kiriting: '))
# chegirma = 0
# if harid > 100000:
#     chegirma = harid * 0.1
#     print(f"ushbu summadagi haridingizga chegirma: {chegirma} ")
# elif harid < 100000:
#     print(f"Ushbu {harid} summadagi haridingizga chegirma kozda tutilmagan")

"""5 Ex"""

# vazn = int(input("Vaznizni kiriting: "))
# boy = int(input("boyizni kiriting: "))
# ideal_vazn = boy - 100

# if vazn == ideal_vazn:
#     print("siz ideal vazndasiz")
# elif vazn > ideal_vazn:
#     n = ideal_vazn - vazn
#     print(f"siz {n} vaznga ozishiz kere")
# elif vazn < ideal_vazn:
#     v = ideal_vazn - vazn
#     print(f"siz {v} kg ga semirishiz kere" )
"""7 Ex"""

# h = int(input("harid qiymatini kiriting: "))
# ch = 0
# if h > 500:
#     ch = h * 0.05
#     print(f"ushbu {h} somlik haridingizga chegirma: {ch}")
# elif h > 1000:
#     ch = h * 0.1
#     print(f"ushbu {h} somlik haridingizga chegirma: {ch}")

"""8-ex"""
# x = int(input("1 dan 12 gacha son kiriting: "))
# 1 < x < 12
# if 1 <= x <= 3:
#     print("qish fasli")
# elif 4 <= x <= 6:
#     print("bahor fasli")
# elif 7 <= x <= 9:
#     print("kuz fasli")
# elif 9 <= x <= 12:
#     print("qish fasli")
# else:
#     print("ERROR! siz kiritgan son hech qaysi shartni qanotlantirmidi")

"""9 Ex"""
# a = int(input("Son kiriting: "))
# b = int(input("Son kiriting: "))
# c = int(input("Son kiriting: "))

# o = (a + b + c) / 3
# o = int(o)
# print(o)

"""10 Ex""""
# a = int(input("Son kiriting: "))
# b = int(input("Son kiriting: "))
# c = int(input("Son kiriting: "))
# o = min(a, b, c)
# print(o)

""""11 Ex""""
# a = int(input("uchburchak tomonini kiriting(a):"))
# b = int(input("uchburchak tomonini kiriting (b):"))
# c = int(input("uchburchak tomonini kiriting (c):"))

# if c  2 == a  2 + b ** 2: 
#     print(f"uchburchak togri burchakli")
# else:
#     print(f"uchburchak togri burchakli bola olmidi")

"""Ex 12"""
# a = int(input("write a number:"))
# b = int(input("write a number:"))
# D = a  2 - b  2
# C = (a - b) ** 2
# if D > C:
#     print("kvadratlarining ayirmasi katta")
# else :
#     print("ayirmasining kvadratlari katta")
 
# a = int(input("Write a number"))
# if a >= 0:
#     if a % 2 == 0:
#         print("juft son")
#     elif a % 10 == 7:
#         print("oxirgi raqami 7 bilan tugaydi")
#     else :
#         print("juft ham emas 7 raqami bilan tugamaydi ham")
# else :
#     print("natural son emas")

"""14 Ex""""
# a = int(input("Son kiriting: "))
# b = int(input("Son kiriting: "))
# c = int(input("Son kiriting: "))
# o = max(a, b, c)
# print(o)
 #2 
 # #Calculate the additional fee added for seniority, if the seniority is from 2 to 5 years, 2% will be added, if from 5 to 10 years, 5% will be added. Enter salary and seniority from the keyboard, output bonus and total salary.




"""MIDDLE LEVEL""" 

# # #1
# # #Enter two numbers from the keyboard. Determine whether the sum of the squares of these numbers is greater or the sum of the squares is greater. Display the answer in the form of a message.
# # Store input numbers
# num1 = input('Enter first number: ')
# num2 = input('Enter second number: ')

# # Add two numbers
# sum = float(num1) + float(num2)


# print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

# #4
# # #Determine whether a triangle with sides a, b, c is an equilateral triangle?
# def is_valid_triangle(a,b,c):
#     if a+b>=c and b+c>=a and c+a>=b:
#         return True
#     else:
#         return False
# def type_of_triangle(a,b,c):
#     if a==b and b==c:
#         print('Triangle is Equilateral.')
#     elif a==b or b==c or a==c:
#         print('Triangle is Isosceles.')
#     else:
#         print('Triangle is Scalane')
        

