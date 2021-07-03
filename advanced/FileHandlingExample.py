f = open('MyIntro', 'r')

print(f.readline(), end="#")
print(f.readline())

f1 = open('abc.txt', 'a')
f1.write('Something')

for data in f:
    f1.write(data)