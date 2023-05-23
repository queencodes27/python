import random
m = [random.randint(-100, 100) for i in range(100)]
x = filter(lambda x: x < 0, m)

print (x)


x = [13, 14, 90, -3, -2, -9, 0, 2, 0]
m = list(filter(lambda x: x < 0 and x % 2 == 1 ,x))
print (m)