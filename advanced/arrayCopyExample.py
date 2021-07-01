from numpy import *

arr1 = array( [1, 2, 3, 4, 5])

# arr2 = arr1
arr2 = arr1.view()  # same array - shallow copy
arr2 = arr1.copy() # deep copy

arr1[1] = 7

print(arr1)
print(arr2)

print('Printing address for arrays ')
print(id(arr1))
print(id(arr2))
