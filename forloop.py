"""FOR loop"""
#for i in range(10)  # for : cycle i = variable , range() = function

#print () # by default bu yerda new line bor 
#print (i, end=/n)

"""
1.
Ikkita butun son A va B (A<B) berilgan. 
Shu sonlar oralig`ida joylashgan barcha butun sonlarni o`sish tartibida toping 
( shu sonlar lan birgalikda) va ularni soni N ni ham.

# """
# a = int(input("write a number: "))
# b = int(input("write a number: "))
# n = 0

# for i in range (a, b+1):
#     print (a, end=',')
#     n += 1  # n = n + 1
#     print ()
# print(f "{n} numbers exist btw {a} and {b}")
"""
2. Ikkita butun son A va B (A<B) berilgan. 
Shu sonlar oralig`ida joylashgan barcha butun sonlarni kamayish tartibida toping 
( bu sonlarni hisobga olmay) va ularni soni N ni ham.

"""
"""
6.
Haqiqiy son A(>1) berilgan. 1+1/2+1/3+...+1/N yig`indisi A dan katta bo`ladigan, 
eng kichik N butun sonni va ushbu summani toping.
"""
# a = int(input("write a number: "))
# n = int(input("write a number: "))
# s = 0

# for i in range(1, 1_000_000):
#     s = s + 1 / i
#     print (s, end = ' ')
#     if a < s :
#         break 
# print (i) 


"""
7.
Haqiqiy son N(>1) berilgan. 1∙2∙ ∙N ko`paytmasini toping.
# """
# x = int(input("write a number: "))
# n = 1
# for i in range (1, x + 1):
#     n = n * i 
# print(n)

"""
8. 
Haqiqiy son N(>1) berilgan. 2 ·1/(2) · 1/(3) ·...· 1/(N) ko`paytmasini
toping.
"""
# x = int(input("give a number: "))
# n = 2
# for i in range (2, x + 1):
#     n = n * 1/i ;
# print (n) 

"""
9.
Haqiqiy son X va butun son N(>0) berilgan. 1 + X+X2/2 +... + XN/N
qiymatini toping.
"""
# x = int(input ("give a number:  "))
# n = 1

# for i in range (1, n+1):
#     n = n + ((x**1)/i)
# print (n)
     
""" 
10.
Haqiqiy son X va butun son N(>0) berilgan. X –X3/3+X5/5 +...+(–
1)NX2N+1/(2N+1) qiymatini toping.
"""

# x = int(input("give a number:  "))
# n = int(input("give a number:  "))
# s = 0
# for i in range(1, n+1):
#     s = s + pow(-1, i) * pow(x, 2 * i) / 2 * i
#     print(s)
# print(s)
"""
11.
Haqiqiy son X va butun son N(>0) berilgan. 1 –X2/2 + X4/4 –... + (–1)
NX2N/(2N) qiymatini toping.
"""
x = int(input("give a number:  "))
n = int(input("give a number:  "))
s = 1 # 0 bomidi chunki mahrada 0 bomidi
for i in range(1, n+1):
    s = s + pow(-1, i) * pow(x, 2 * n) / (2 * n)
    print(s)
print(s)

"""
12.
Haqiqiy son X(|X|<1) va butun son N(>0) berilgan. X – X2/2 + X3/3 – + (–1)N–1XN/N qiymatini toping. 
Topilgan son 1+X nuqtada ln funksiyasining yaqinlashgan qiymati bo`ladi.
"""


"""
13
10 dan N gacha bo`lgan natural sonlar berilgan. 5 ga karrali bo`lgan toq sonlari chop eting.
"""
# n = int(input("give a number: "))

# for i in range(10, n):
#     if i % 5 == 0 and i % 2 == 1 :
#         print(i)

"""
19.

"""

# a = 0
# for i in range(12, 81):
#     a = a + i  2
# print(a)

"""
20.
"""

# a = 0
# for i in range(22, 89):
#     a = a - i  2
# print(a)

"""
21.
"""

# A = int(input("Write a number:"))
# N = int(input("Write a number:"))
# for i in range(1, N + 1):
#     x = (i  2) - A  2
#     print(x)

"""
23.
"""

# A = int(input("Write a number:"))
# N = int(input("Write a number:"))
# for i in range(1, A + 1):
#     x = i  N
#     print(x)

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

"""
28 
"""

# my_list = [ ]
# N = int(input("Write a number:"))
# for i in range(10, N + 1):
#     if i % 5 == 0 :
#         my_list.append(i)
# print(my_list)

"""
32
"""

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