"""
FUCTION IN PYTHON
"""
"""
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

Return statement simply returns the values as output
 whereas print() function simply print the value.
 (return variable types:handle, integer, object, or string)

"""
# def my_function():
#   print("Hello from a function")

# my_function()
"""
Arguments
Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. 
You can add as many arguments as you want, just separate them with a comma
"""    
# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

import random

# list1 = [random.randint(1,100) for i in range(20)]
# list2 = [random.randint(1,100) for i in range(20)]
# n = max(list1)
# b = max(list2)

# def my_function(my_list1:list, my_list2:list):
#   print(my_list1)
#   print(my_list2)
#   print(n)
#   print(b)
# my_function(list1, list2)



def function1(x,y):
    return(x+y)
x = function1(4,7)
print(x)



print(primenumbers(5, 15))
# a = 2
# print(pow())
def my_pow(number:int, degree:int):
     return number ** degree


x = my_pow(3, 2)

c = x * 2
print(c)
         

# x = input(">>> ").split()
# def find_negatives(l):
#    list = []
#    for n in l:
#        if int(n) < 0 :
#            list.append(int(n))
#    return list
           
# print(find_negatives(x))


def func1(func:int):
    def wrapper(*args, **kwargs):
        x = func(*args, **kwargs)
        if x == 0:
                print("not divided by 0")
        if a % b
    return c
