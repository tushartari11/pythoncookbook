a = 5
b = 2

try:
    a = int(input("Enter a number a: "))
    b = int(input("Enter a number b: "))
    print(a / b)
except ZeroDivisionError as e:
    print(" you cannot divide a number by zero : ", e)
except ValueError as e:
    print(" Invalid Input : ", e)
except Exception as e:
    print(" Something went wrong : ", e)
finally:
    print("resource closed")
