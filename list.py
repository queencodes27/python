""" PYTHON LIST """

# n = [] # shu kvadratniy skobka list degani
# x = ' '  # bu string chiqoradi

n = [ 12, 9999,-2.5, 0, 1, 78, 98,1]
m = [ "isksksks" , 1, 3, 6, 8 ]
# n.append(7) # it adds character to the list
# n.insert (2, "hwkhw") # THIS remove character in index 2 and inputs given string
# n.remove(True) # removes the character from the list 
#n.extend(m) # it adds list from m to n and extends the list

# n.sort() # sorts from lower to bigger. It has to be integer or string in one list on order to be sorted
# n.sort(reverse=True) # it reverses 
# l = sorted(n)  # bu list'i nusqasini oladi va sort qilip qaytarip yuboradi
# print (n, l)  # difference btw sort vs sorted: sort method in list gived output with changes in indexes of the list
 # Sorted in building function doesn't make changes in indexes ofc haracters
# a = m.copy() # it copiest the list into variable a
# a.clear() # clears the list
# print (a)
# c = m.count("k") # counts the number of characters in list
# n.remove (78) # removes the number itself not index
# n.pop (9)  # deletes the index

# x = [1, 2, 4, [5, 6,7], "kdk, ["p"], sks" ]
# x.pop[4][1]
# print (x)  

"""PYTHON TUPLE"""
""" PYTHON TUPLE it is a list with () and never changes. which means stable list and you can't add or remove"""
v = (1, 5, 6, 89, "hdhdhd", [8, [0,9,9890,0], 0 ], ["l"], 0)

print (type(v), v[5][1][1])
print(v.count(1)) 

v = list(v) # this converts tuple into the editable list
print (v)