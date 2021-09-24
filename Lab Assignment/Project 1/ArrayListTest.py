# import numpy as np
from ArrayList import ArrayList

i = 6
n = 10
for k in range(n, i, -1):
    print(k)


arraylist = ArrayList()

arraylist.append("a")
arraylist.append("b")
arraylist.append("c")
arraylist.append("d")
arraylist.append("e")
arraylist.append("f")
arraylist.append("g")
arraylist.append("h")

print(arraylist)
arraylist.remove(0)
print(arraylist)
arraylist.remove(0)
print(arraylist)
arraylist.remove(1)
print(arraylist)
arraylist.remove(1)
print(arraylist)
arraylist.remove(1)
print(arraylist)
arraylist.remove(1)
print(arraylist)

