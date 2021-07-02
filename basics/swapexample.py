a = 5
b = 6

print(a)
print(b)

a = a ^ b
b = a ^ b
a = a ^ b

print('After swap')
print(a)
print(b)

a, b = b, a

print('After python swap')
print(a)
print(b)
