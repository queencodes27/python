# Python OS module provides easy functions that allow us to interact and
# get Operating System information and even control processes up to a limit.
# It is a standard library within Python 3 installation. You just need to import it to use. 

import os
from pathlib import Path


# from datetime 
# print(os.getcwd()) : prints current working dir
# print(os.listdir()) : prints  list of dir 
# os.mkdir
# os.stat : this prints out information about the file such as st.mtime, st.size=20 : string size in the file
# os.walk()

"""
os.path.basename(path())
print(os.basename(path))

uname : 
fchown: Change the owner and group id of the file given by fd to the numeric uid and gid. 
fsync: force write files with filedescriptor fd to disk. 
pipe : create a pipe. return a pair of file descriptors (r, w) usable for reading and writing

"""

import time
from random import randint
from dataclasses import dataclass, field, asdict, astuple
from itertools import groupby, chain, count, cycle, dropwhile, takewhile

# m = [ i for i in range (1, 11)]
# x = groupby(m, key=lambda x: x >= 5)
# print(x)

# l =["ali", "alex","toshmat", "azim"]
# print(list(chain.from_iterable(l)))


"""
    Функция chain() модуля itertools создает итератор, 
    который возвращает элементы из первой iterables, 
    пока она не будет исчерпана, а затем переходит 
    к следующей iterables, пока все итерируемые последовательности 
    не будут исчерпаны.
"""

x = ["ali", "bobur", "sancho"]
c = cycle(x)
for i in range(20):
    print (next(c))
    print (f"{i+1}: {next(c)}")
