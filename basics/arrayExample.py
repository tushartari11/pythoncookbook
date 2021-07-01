from array import *

vals = array('i',[5, 9, -2, 4, 2])

for i in range(len(vals)):
    print(vals[i])

"""iterable """
print(' -------------------- using iterables ----------- ')
for e in vals:
    print(e)

newArr = array(vals.typecode, ( a*a for a in vals))

"""iterable """
print(' -------------------- using copied array ----------- ')
for n in newArr:
    print(n)