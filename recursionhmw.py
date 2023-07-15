#homework #recursion
'''
1. Birdan N gacha bo'lgan sonlar kavatiratini ko'rsatuvchi dastur tuzing.
2. listdagi raqamlar yig'indisini hisoblash dastur.
3. ikki sonni EKUB ni aniqlovchi dastur

#homework #recursion
nums = (1, 2, 3, 4, 5, 6, 7)
Berilgan butun sonlar ro‘yxatidagi barcha sonlarni KUBINI hisoblovchi dastur tuzing, Pythondagi map dan fodalangan holda 
OUTPUT: [1, 8, 27, 64, 125, 216, 343]


students = [
    {'name': 'John', 'age': 18, 'grade': 'A'},
    {'name': 'Emma', 'age': 19, 'grade': 'B'},
    {'name': 'Alice', 'age': 17, 'grade': 'A'},
    {'name': 'Michael', 'age': 20, 'grade': 'C'}
]

studenlar haqida ma'lumot berilgan shularni filter() funksiyasini ishlatgan holda 18 yoshga teng yoki kattalarini ro'yxatini qaytaring

OUTPUT: [{'name': 'John', 'age': 18, 'grade': 'A'}, {'name': 'Emma', 'age': 19, 'grade': 'B'}, {'name': 'Michael', 'age': 20, 'grade': 'C'}]

'''

# 1. Birdan N gacha bo'lgan sonlar kavatiratini ko'rsatuvchi dastur tuzing.

# def myfunc(n:int):
#      list = []
#      if n == 1:
#           return 1
#      print (n**2, end=' ')
#      return myfunc(n-1)
#     #  list.append()
# print(myfunc(7))


# 2. listdagi raqamlar yig'indisini hisoblash dastur.


# def getsum(numbers):
#     if len(numbers) == 0:
#         return 0
#     return numbers[0] + getsum(numbers[1:])
# list=[26, 1997, 8, 1, 0]
# print(getsum(list))

     
# 3. ikki sonni EKUB ni aniqlovchi dastur 
# FIND THE GREAT COMMON DIVISOR

# def gcd(a, b):
#     if a == b:
#         return a
#     elif a < b:
#         return gcd(b,a)
#     else:
#         return gcd(b, a -b)
# print(gcd(5,20))

# # 2'nd way for finding gcd
# def ekub(number1:int, number2:int):
#     if number2 ==0:
#         return number1
#     return ekub(number2, number1 % number2)
# print(ekub(18,12))
# # # 4.Studenlar haqida ma'lumot berilgan shularni filter() funksiyasini ishlatgan 
# holda 18 yoshga teng yoki kattalarini ro'yxatini qaytaring

# students = [
#     {'name': 'John', 'age': 18, 'grade': 'A'},
#     {'name': 'Emma', 'age': 19, 'grade': 'B'},
#     {'name': 'Alice', 'age': 17, 'grade': 'A'},
#     {'name': 'Michael', 'age': 20, 'grade': 'C'}
# ]

# m = list(filter(lambda x: x['age']>=18, students))
# print(m)

# # 5.MApping
# nums = (1, 2, 3, 4, 5, 6, 7)
# print(nums)
# x = list(map(lambda z:z ** 3,nums))
# print(x)

a = [1, 2, 3, 4, 5, 6]
print(filter[lambda x : x % 2 == 0, a])
