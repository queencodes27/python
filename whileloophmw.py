"""
1.
Ikkita butun son A va B (A<B) berilgan. 
Shu sonlar oralig`ida joylashgan barcha butun sonlarni o`sish tartibida toping 
( shu sonlar lan birgalikda) va ularni soni N ni ham.
"""

# a = int(input("write a number: "))
# b = int(input("write a number: "))
# n = 0

# while a < b :
#     n += 1
#     a += 1
#     print(a)
# print(n)
"""
2. Ikkita butun son A va B (A<B) berilgan. 
Shu sonlar oralig`ida joylashgan barcha butun sonlarni kamayish tartibida toping 
( bu sonlarni hisobga olmay) va ularni soni N ni ham.

"""
# a = int(input("write a number: "))
# b = int(input("write a number: "))
# n = 0

# while a < b :
#     n += 1
#     b -= 1
#     print(b)
# print(n)

"""
3. Haqiqiy son A va butun son N(>0) berilgan. 
A ning N chi darjasini toping: AN = A·A··A(A soni N martta ko`paytiriladi).
"""
# a = int(input("write a number: "))
# n = int(input("write a number: "))
# y = a
# s = 1

# while s < n:
#     y = y*a
#     s+=1
# print(y)

"""
4. 
Haqiqiy son A va butun son N(>0) berilgan. 
A ning barcha 1 dan N gacha bo`lgan darajalarini toping.
"""
# a = int(input("write a number: "))
# n = int(input("write a number: "))
# y = a
# s = 1
# print(a)
# while s < n:
#     y = y*a
#     print(y)
#     s+=1
"""
5.
Haqiqiy son A va butun son N(>0) berilgan. 
Chiqaring: 1+A+A2+A3+ + AN.
"""
# a = int(input("write a number: "))
# n = int(input("write a number: "))
# i = 0
# s = 1
# while i < n:
#      i += 1
#      s += a ** i
#      print(s)
     
"""5'th question with for loop"""   
     
# a = int(input('Son Kiriting: '))
# n = int(input('Son Kiriting: '))
# s = 0 
# for i in range(0, n + 1):
#     s += a ** i
# print('Natija', s) 
"""
6. 
Haqiqiy son A(>1) berilgan. 1+1/2+1/3+...+1/N yig`indisi 
A dan katta bo`ladigan, eng kichik N butun sonni va ushbu summani toping.
"""

# a = int(input("write a number: "))
# n = int(input("write a number: "))
# i = 1
# s = 1
# while i < n:
#      s += a/i
#      i+=1
#      print(s)

"""7.
Haqiqiy son N(>1) berilgan. 1∙2∙ ∙N ko`paytmasini toping."""
# n = int(input())
# i = 0
# s = 1
# while i < n:
#     s *= 1 + i
#     i += 1
#     print(s)

# n = int(input())
# i = 2
# s = 2
# while i <= n:
#     s *= 1/i
#     i += 1
#     print(s)

# x = int(input())    
# n = int(input())
# i = 2
# s = 1 + x
# while  i <= n:
#      s += (x**i)/i
#      i += 1
#      print(s)  
     
     
"""10)
Haqiqiy son X va butun son N(>0) berilgan. X –X3/3+X5/5 +...+(–
1)NX2N+1/(2N+1) qiymatini toping."""

# x = int(input("give a number:  "))
# n = int(input("give a number:  "))
# s = 0
# i = 0
# while i <= n:
#     s = s + pow(-1, i) * pow(x, 2 * i +1) / 2 * i + 1
#     i += 1
#     print(s)
# print(s)

"""11
Haqiqiy son X va butun son N(>0) berilgan. 1 –X2/2 + X4/4 –... + (–1)
NX2N/(2N) qiymatini toping."""

# x = int(input())
# n = int(input())
# s = 0
# i = 0
# while i <= n:
#     s = s + pow(-1, i) * pow(x, 2*i) / 2*n    
#     i += 1
#     print(s)
# print(s)

"""13)
10 dan N gacha bo`lgan natural sonlar berilgan. 
5 ga karrali bo`lgan toq sonlari chop eting."""

# n = int(input())
# i = 10
# while i <= n:
#     if i % 5 == 0:
#         print(i)
#     i += 1
  
"""14)
11 dan 99 gacha bo`lgan sonlarni kvadratini chiqaring.
"""  
# for i in range(11, 99):
#     i = i**2
#     print(i)
  
"""15
Berilgan n uchun n! va 2n ni bitta siklda chiqaring.
"""  
# n = int(input())
# i = 1
# s = 1
# while i <= n:
#     s = s * i
#     i += 1
#     print(s)
# print(2**n)

"""16
10 dan N gacha bo`lgan natural sonlar berilgan. Ular orasidan butun
o`nxonalik sonlardan eng katta sonni toping.
"""
# n = int(input())
# i = 10
# s = 0
# while i <= n:
#     if i % 10 == 0:
#         s = i
#     i += 1
# print(s)

"""17
10 dan N gacha bo`lgan natural sonlar berilgan. Natural son uchun
uning birinchi raqamini va uning raqamlari yig`indisini toping.
"""
# n = int(input())
# i = 10
# s = 0
# while i <= n:
#     s = s + i
#     i += 1
# print(s)

"""18
Berilgan soni palindrom deb xisoblasa bo`ladimi,
ya’ni o`ngdan chapga va chapdan o`ngga bir xil o`qiladimi.
Misol: 123321, 202, 9889, 5555.
"""
# n = int(input())
# x = str(n)
# x = x[::-1]
# if str(n) == x:
#     print("Yes it is")
# else:
#     print("No it is not")

"""19
12 dan 80 gacha bo`lgan sonlarni kvadratini yig`indisini chiqaring."""

# i = 12
# s = 0
# while i <= 80:
#     s += i**2 
#     i+=1
#     print(s)

"""20 
22 dan 88 gacha bo`lgan sonlarni kvadratini ayirmasini chiqaring."""

# i = 22
# s = i **2
# while i < 88:
#     i += 1
#     s -= i**2
#     print(s)

"""21
Haqiqiy son A va 1 dan N(>0) gacha bo`lgan natural sonlar berilgan. 
N natural sonlari kvadrati va A ning kvadrati ayirmasini toping."""


# A = int(input("Write a number:"))
# N = int(input("Write a number:"))
# for i in range(1, N + 1):
#     x = (i ** 2) - A ** 2
#     print(x)
"""
22.   ASK HIM WHAT IS THIS?
10 dan N gacha bo`lgan natural sonlar berilgan.
Ular orasidan eng kichik butun o`nxonalik sonni toping.
"""

# n = int(input("Write a number:"))
# for i in range (10, n + 1):
#         print (i)

"""
23.
A sonini butun N darajaga oshiring
"""


# A = int(input("Write a number:"))
# N = int(input("Write a number:"))
# for i in range(1, A + 1):
#     x = i  N
#     print(x)

"""
24. Berilgan sonni faktorialini hisoblang. N sonining faktorialini quyidagi
formula bo`yicha xisoblang: N!=1*2*3*...N

"""
# n = int(input())
# i = 1
# s = 1
# while i <= n:
#     s = s * i
#     i += 1
#     print(s)

"""
25.
"""
# A = int(input("Write a number:"))
# s = 0
# for i in range(1, A + 1):
#     s = s + (i  2)
# print(s)

"""
26.

"""

# A = int(input("Write a number:"))
# x = 0
# y = 0
# for i in range(2, A + 1, 2):
#         x = x +  i  2
# for i in range(1, A + 1, 2):
#         y = y +  i  3
# s = x + y
# print(s)

"""27.
5 ga karrali bo`lmagan va 3 ga karrali bo`lgan sonlarni toping,
shuningdek 5 ga karrali bo`lmagan va 3 ga karrali bo`lgan sonlarni summasini toping.
"""
# n = int(input("Write a number: "))
# i = 1
# while i <= n:
#     if i % 5 == 1 and i % 3 == 0:
#         print(i) 
#     i += 1

"""
28 
"""

# my_list = [ ]
# N = int(input("Write a number:"))
# for i in range(10, N + 1):
#     if i % 5 == 0 :
#         my_list.append(i)
# print(my_list)

"""29
Berilgan natural son ikkining darajasi bo`la oladimi?
"""
# N = int(input("Write a number:"))

# print (" Yes, the number is power of 2 . |" , "n ** 2 = ", N**2)
 

"""
30.   # ASK THIS!!!
Berilgan sonni ko`paytuvchilarga ajrating.
"""
# n = int(input("Write a number:"))
# a = int(input("Write a number:"))

# print (n/)

"""
31.
Bir sonini ham inobatga olgan holda, bo`luvchilari yig`indisiga teng bo`lgan son tub son deyiladi. 
2 dan x oralig`igacha bo`lgan sonlar ichidan tub sonlarni toping va chop qiling.
"""
# n = int(input())
# i = 2
# while i <= n:
#     if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 :
#         print(i) 
#     i += 1

# m = int(input("boshlanish sonni kiriting:"))
# n = int(input("oxirgi sonni kiriting:"))
# s = 0  
# for i in range(m, n + 1):
#     s = s + i  2
# print(s)

"""
33 
"""
# m = int(input("boshlanish sonni kiriting:"))
# n = int(input("oxirgi sonni kiriting:"))
# s = 0
# for i in range(m, n + 1):
#     if i % 2 == 1:
#         s = s + i  2
# print(s)

# 34 - misol
# s = 1
# for i in range(-80, 81):
#     if i % 7 == 0 and i % 2 == 1:
#         s = s * i
# print(s)




"""Yuqori bosqich"""



"""4
Agar berilgan soni o`ngdan chapga va chapdan o`ngga bir xil o`qilsa palindrom deb ataymiz.
100 dan kichik palindrom sonlarni toping."""

# i = 0
# while i <= 100:
#     i = str(i)
#     x = str(i)
#     x = x[::-1]
#     if x == i:
#         print(i)
#     i = int(i)
#     i += 1
    
"""5.
"""
# i = 0
# while i <= 100:
#     i = str(i)
#     x = str(i)
#     x = x[::-1]
#     if x == i:
#         print(i)
#     i = int(i)
#     i += 1


"""14. M darajaga oshirilgan 1 dan n gacha bo`lgan sonlarning yig`indisini"""
# n = int(input("num:"))
# m = int(input("power:"))
# i = 1
# s = 0
# while i <= n:
#     s += i**m
#     i+=1
#     print(s) 
