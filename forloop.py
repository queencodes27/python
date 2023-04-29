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
a = int(input("write a number: "))
n = int(input("write a number: "))
s = 0

for i in range(n)


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
# x = int(input("give a number:  "))
# n = int(input("give a number:  "))
# s = 0
# for i in range(1, n+1):
#     s = s + pow(-1, i) * pow(x, 2 * n) / (2 * n)
#     print(s)
# print(s)

"""
13.
10 dan N gacha bo`lgan natural sonlar berilgan. 5 ga karrali bo`lgan toq sonlari chop eting.
"""
# n = int(input("give a number: "))

# for i in range(10, n):
#     if i % 5 == 0 and i % 2 == 1 :
#         print(i)