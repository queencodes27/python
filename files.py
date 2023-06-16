"""
.exe
.png
.jpg
.txt
.svg
"""
# my_file = open("test.txt", "x" ) #open = key
# print(my_file.readline(2))  # takes string on 2'nd index
# my_file.close()


dict = {}
with open("mypwd.txt", "r" ) as file:
    for line in file:
        if line:
            key, value = map(str.strip, line.split(";"))
            dict[key] = value
    print(dict)
t = {}
for i in t.keys():
    t[i] += 1
else:
    t[i] = 1
x = sorted(t.items, key = lambda i: i[1], reverse = True)z = x[ : 11]


     
    
    
      