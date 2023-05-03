import random
# n = int(input("Write a number:"))
# l =[]

# for i in range (20):
#     l.append(random.randint(1,100))
#     print(l)
# n = l[0]  # max_item
# while i > l:
#     n = l
#     print (" max number", n)

# l = []  
   
# for i in range (21):
#     l.append(random.randint(1,100))
# print(l)
# for i in l:
#     if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 :
#         print(i) 

"""
2'nd way to solve 
""" 
l = []       
for i in range(0, 20):
    l.append(random.randint(1,100)) # tasadofiy sonlarini list qip chiqarip beradi
print(l)

x = []

for i in l:
    n = 0
    for k in range (1, i + 1):
        if  i % k == 0:
            n += 1
    if n == 2: # chislo delitelya = boluvchi
        # x += 1
        x.append(i)
    else:
        n = 0
print(x)
        
    
# my_list = [random.randint(1,100) for i in range(20)]
# print(my_list)