# A (x,y)
x = int(input ("write x number: "))
y = int(input ("write x number: "))

if x > 0 and  y > 0 :
    print("it lays on 1 coordinate")
elif x < 0 and y > 0 :
    print("it lays on 2 coordinate")
elif x > 0 and y < 0 :
    print ("it lays on 3'rd coordinate")
elif x > 0 and y < 0 :
    print("it lays on 4th coordinate")
else:
    print ("It lays on 0 coordinate")