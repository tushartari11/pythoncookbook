from math import isqrt

num = int(input("Please enter a number : "))

for i in range(2, isqrt(num)):
    print("looping ", i, " time")
    if num % i == 0:
        print('Not prime')
        break;

else:
    print("Prime")
