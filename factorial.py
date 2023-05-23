# def main(n:int):
#       if n == 0:
#             return 0
#       print(n)
#       return  main(n - 1) 

# print(main(8))

# def main(n):
#     f1
# or i in range (i)

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
print(factorial(5))