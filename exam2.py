"""
Условие
Даны три целых числа. Определите, сколько среди них совпадающих. 
Программа должна вывести одно из чисел: 
3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).
"""

# a = int(input("your number: "))
# b = int(input("write a number: "))
# c = int(input("write a number: "))
# if a == b or  a == c:
#     print("equals to 3")
# elif not a == b  or a == c:
#     print("equals to 2")
# else:
#     print("equals to 0")

#2

# a = int(input("your number: "))
# b = int(input("your number: "))
# print (a ** b )

#3

# a = int(input("your number: "))
# if a % 2 == 0:
#     print("True")
# else:
#     print("false")

#4
# a = int(input("your number: "))
# if a > 99 and a < 1000: 
#     print(int(str(a)[-1])) 
#     # print(a % 10)
# else:
#     print("False")
# #5
# a = int(input("your number: "))
# if a % 2 == 0:
#     print("juft")
# else :
#     print("toq")
# 6
# n = 5
# for i in range (1, n+1):
#     for x in range (1, i + 1):
#         print(x, end=" ")
#     print()

# 7
# n = 5
# for i in range (1, n+1):
#     for x in range (1, i + 1):
#         print(x, end=" ")
#     print()
# for i in range (1, n+1):
#     for x in range (1, n-i+1):
#         print(x, end=" ")
#     print()
# 8
#  minimum son
my_list = [1, 7, 8, 9, 0]
a = my_list[0]
for x in my_list:
    if x < a:
        a = x
print(a)

# 9
# maximum son 
# my_list = [1, 7, 8, 9, 0]
# a = my_list[0]
# for x in my_list:
#     if x > a:
#         a = x
# print(a)
     
# 10

# my_list = [1, 7, 8, 9, 0]
# sum_items = 0
# for x in my_list:
#     sum_items += 1
# print(sum_items / len(my_list))
    
#11

# my_list = [1, 7, 8, 9, 0]
# sum_items = 0
# d = 0
# for x in my_list:
#     sum_items += 1
#     d += 1
# print(sum_items / d)

# 12

# x = [ 16, 67, 90, 17, 11, 78, 988676]
# # y = [i // 10 % 10 for i in x]
# for i in x:
#     s = i // 10
#     print(s)
#     a = s % 10
#     print(a)
# # print(y)

#13
# import random
# m = (random.randint(1,100)for i in range(20))

#14

my_list = ["_aziz_", "_sarvar_","_ali_", "_islom_", "_maruf_"]
n = [(i.replace("_", " "))for i in my_list]

print(n)