
"""
Task1.
Create a function through recursion. The user is required to enter numbers, 
and if the number entered is not equal to 0, the function returns the 
numbers entered by the user in reverse order, but does not output 0.
"""

# def my_func():
#     n = int(input("enter #: "))
#     if  n == 0:
#         return n
#     else:
#         my_func()
#         print(n)
# my_func()

#2'nd way to solve
# def reverse():
#     x = int(input(""))
#     if x != 0:
#         reverse()
#         print(x)
# reverse()

"""
## Task 2
Create a function that finds the second Max,
The user is required to enter numbers and
function if the number entered is not equal to 0
Let the second Max enter the numbers entered by the user. 
It is necessary to use while in the function !!!

"""
# def sec_max():
#     l= []
#     while True:
#        n = int(input("son:"))
#        if  n == 0:
#            break
#        else:
#            l.append(n)
#     l.sort()
#     l.reverse()
#     print(l)
#     return l[1]
# x = sec_max()
# print(x)




"""
Create a file numbers.txt and write numbers from 10 to 500 in it as follows

"""        

# with open("numbers.txt", "w" ) as f:
#     for i in range (10, 500, 11):
#         # print(i)
#         f.write(f"{str(i)} \n")





"""
## Task 4
write a lambda function which finds 3 smallest integers
"""
# input = [3,7,9]
# get_smallest = lambda a, b, c : min(a,b,c) 
# print(get_smallest(3,7,9))

"""
task. 5
Extract all parts of the numbers in the tuple below through the map, 
and the result is also in the form of a tuple
"""
# Input: ( 2.88, -1.75, 100.55 )
# # Output: (2, -1, 100)
my_list = ( 2.88, -1.75, 100.55 )
x = tuple(map(lambda i:int(i), my_list))
print(x)

"""
Task6. 
**Sizlarga insonlarni ulgan va tugilgan yillari berilgan,**

 **[(1920, 1938), (1911, 1944), (1920, 1955), (1938, 1939), (1900,2000), (1900,2000), (1900,2000), (1900,2000), (1900,2000)]**

**Qaysi yilda eng kup inson trik bulganini toping**
"""
# def longlived(xammasi, tirik):
#     dict = {}
#     born = []
#     dead = []
#     year = [(1920, 1938), (1911, 1944), (1920, 1955), (1938, 1939), (1900,2000), (1900,2000), (1900,2000), (1900,2000), (1900,2000)]
#     year = dict()
#     for i in year:
        
        
"""
Task 7.
Create a function that converts a date from MM/DD/YYYY format to YYYYMMDD.

"""
        
"""
Task 8.
While: The athlete covered a distance of 1 m when running on the 1st day. 
Every day he runs twice as much as the previous day. 
How many days does an athlete cover a distance of more than 1000 m?
"""
# distance = 1
# days = 1
# while distance <= 1000:
#     distance *= 2
#     days += 1
# print(f"{days}, {distance}")


