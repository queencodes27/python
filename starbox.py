"""
STAR BOX
"""
import random

l = int(input(": "))
# for i in range(l):
#     for x in range(l):
#         if i == 0 or x == 0 or i == l - 1  or  x == l - 1 or i + x == l - 1 or i + 1 > l - x: #i + 1 < l - x : star filled right top triangle
#             print("$ ", end="")
#         else:
#             print("  ", end="")
#     print()
# pass
# for i in range(l):
#     print(" "*(l - i - 1)+ "$" * (i+1))


# for i in range(l):
#     for x in range(l):
#         if i == 0 or x == 0 or i == l - 1  or  x == l - 1 or i + x == l - 1 or x == i:
#             print("$ ", end="")
#         else:
#             print("  ", end="")
#     print()
    
for i in range(l):
    for x in range(l):
        if i == 0 or x == 0 or i == l - 1  or  x == l - 1 or i + x == l - 1 or i == x or  (i>x>l-i-1 and i /2-1) or (i<x<l-i and i < l / 2-1): #i + 1 < l - x : star filled right top triangle
            print("$ ", end="")
        else:
            print("  ", end="")
    print()

    