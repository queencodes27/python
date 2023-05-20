
"""
N🌙, [May 16, 2023 at 10:14:04 AM]:
1. Funksiya ikta son qiymatli argument qabul qiladi.
Vazifa : o'sha sonlar orasidahgi 
tub sonlardan iborat bo'lgan list qiymatli sonlarni qaytarish kerak.

"""

# def primenumbers(start:int, stop:int):
#    l = []
#    for n in range(start, stop+1): 
#       if n > 1:
#          for i in range(2,n):
#                if n % i == 0:
#                   break
#          else:
#                l.append(n)
#    return l



"""
2. misol
Funksiya list tipidagi 1 argument qabul qiladi, 
o'sha listdagi manfiy sonlar ro'yhatini qaytaradi.
"""

# x = [1, 3, -5, 0, -78, -56]
# def find_negatives(l):
#    list = []
#    for n in l:
#        if n < 0 :
#            list.append(n)
#    return list
           
# print(find_negatives(x))
    

"""
3. Misol: funksiya yarat title bilan
"""

# def capital_letters(func):
#     def wrapper(*args, **kwargs):
#         x = func(*args, **kwargs)
#         list = []
#         for i in x:
#             if i.isupper():
#                 list.append(i)
#         return list
#     return wrapper

# @capital_letters
# def titleitbro(s):
#     sozlarim = s.split()
#     list = [soz.capitalize() for soz in sozlarim]

#     return''.join(list)

# print(titleitbro("qachonki siz imkonsiz narsani sevsangiz, o'sha paytda siz haqiqiyni sevasiz"))

"""
Misol 1

l = [random.randint(1,100) for i in range(10)]
print (l)
sort'siz function yaratkin
"""
"""
Misol 2

Function'ga string yoki list qiymat beriladi va siz len'siz fuction yaratkin

"""
"""
Misol 3
Lambda


"""




"""
1.
"""
import random
# 1.option
# def print_list_unsorted():
#     l = [random.randint(1,100) for i in range(10)]
#     print("Unsorted List: ", l)

# print_list_unsorted()

# 2'nd option without method sort

# l = [random.randint(1,100) for i in range(10)]
# print(l)
# def print_sorted_list(numbers:list):
#     for i in range(0, len(numbers)):
#         for j in range(i+1, len(numbers)):
#             if numbers[i] > numbers[j]:
#                 numbers[i] ,numbers[j] = numbers[j], numbers[i]
#     return numbers

# print(print_sorted_list(l))



"""
2.
 """

# def string_length(string):
#     count = 0
#     for letter in string:
#         count += 1
#     return count
# print(string_length("hyenas are not lions. lion never becomes hyena"))

"""
3. 
"""
# list berilgan shu listlarni dagi so'zlarni lambda orqali uzinligiga qarab sartirovka qilib chiqaring

# Input: lst = ['ali', 'python', 'hello', 'uzbekiston', 'start', 'step', 'usa']
# # Output:  ['ali', 'usa', 'step', 'hello', 'start', 'python', 'uzbekiston']



lst = ['ali', 'python', 'hello', 'uzbekiston', 'start', 'step', 'usa']
sortedlist = sorted(lst, key=lambda x:len(x))
print(sortedlist)


"""
4.
1. func1 nomli ikkita int tipli parametirga ega bo'lgan funksiya yarating. Va bu funksiya ikkita sonni bo'linmasini qaytarsin. 
Ush bu funksiyaga decorator func1_deco nomli funksiya yozing. Uni vazifasi agar func1 ga berilgan argumentlarda maxrajdagi qiymat no'lga teng bo'lsa sonni no'lga bo'lib bo'lmasligi haqida ma'lumot chiqarsin.

Masalan:
a = 8
b = 0
c = a / b
bu xolatda sonni no'lga bo'lib bo'lmaydi
"""


# def func1(func):
#     def wrapper(*args, **kwargs):
#         if args[0] > 0 and args[1] > 0:
#            x = func(*args, **kwargs)
#            print(f"Result {x}")
#         elif args[0] == 0 or args [1] == 0:
#             print( " Not divisible by 0" )
#         return 
#     return wrapper

# @func1
# def func1_demo(a:int, b:int):
#     return a / b

# func1_demo(4, 0)
