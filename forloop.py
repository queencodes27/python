"""FOR loop"""
#for i in range(10)  # for : cycle i = variable , range() = function

#print () # by default bu yerda new line bor 
#print (i, end=/n)

"""
1.
Ikkita butun son A va B (A<B) berilgan. 
Shu sonlar oralig`ida joylashgan barcha butun sonlarni o`sish tartibida toping ( shu sonlar lan birgalikda) va ularni soni N ni ham.

"""
a = int(input("write a number: "))
b = int(input("write a number: "))
n = 0

for i in range (a, b+1):
    print (a, end=',')
    n += 1  # n = n + 1
    print ()
    
     