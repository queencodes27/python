import math
#2-misol
# c = int(input(' C ga qiymat bering: '))
# x = int(input('X ga qiymat bering: '))
# t = int(input( 'T ga qiymat bering: '))
# L = pow(math.tan(c),(-2)) + (2 * pow(x,2) + 5) / math.sqrt(c + t)
# print("Result", L)

#3-misol
# y = int(input(' Y ga qiymat bering: '))
# h = int(input('H ga qiymat bering: '))
# a = (math.tan(pow(y,3) - pow(h,4)) + h ** 2) / ( math.sin(h) ** 3 + y )
# print("Result", a)

#5-misol
# y = int(input(' Y ga qiymat bering: '))
# x = int(input('X ga qiymat bering: '))
# z = int(input('Z ga qiymat bering: '))
# c = int(input('C ga qiymat bering: '))

# A = math.tan(pow(x,4) - 6) - math.cos(z + x * y) ** 3
# B = math.cos(pow(x,3) * pow(c,2)) ** 4
# G = A / B
# print("Result", G)

# 6-misol
# y = int(input(' Y ga qiymat bering: '))
# x = int(input('X ga qiymat bering: '))
# t = int(input('T ga qiymat bering: '))
 
# A = math.sin(x) ** 3 + math.log(2 * y + 3 * x)
# B = pow(t,math.exp(1)) + math.sqrt(x)

# P = A / B
# print("Result", P)

#7- misol
# y = int(input(' Y ga qiymat bering: '))
# x = int(input('X ga qiymat bering: '))
# a = int(input('A ga qiymat bering: '))
# b = int(input('B ga qiymat bering: '))

# A = math.sqrt(x + y - a) + math.log(y)
# B = math.atan(b + a)
# T = A / B
# print("Result", T)

#8-misol
# y = int(input(' Y ga qiymat bering: '))
# t = int(input('T ga qiymat bering: '))

# S = (4.351 * pow(y,3) + 2 * t * math.log(t)) / math.sqrt(math.cos(2 * y) + 4.351)

# print("Result", S)

#10-misol
y = int(input(' Y ga qiymat bering: '))
x = int(input('X ga qiymat bering: '))
a = int(input('A ga qiymat bering: '))
b = int(input('B ga qiymat bering: '))
c = int(input('C ga qiymat bering: '))

U  = (pow(math.tan(y),3) + math.sin(x * math.sqrt(b - c)) ** 5) / math.sqrt(a - b + c)

print("Result", U)

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