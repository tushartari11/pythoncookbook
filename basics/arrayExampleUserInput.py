from array import *

arr = array('i', [])

n = int(input('Enter the length of array: '))

for i in range(n):
    x = int(input('Enter the next value: '))
    arr.append(x)

print(arr)

# -------------- searching in array ----

val = int(input('Enter the value to search : '))

counter = 0
for e in arr:
    if e == val:
        print(e)
        break
    counter += 1
print(arr.index(val))
