import math
try:

    n = int(input("Enter a number: "))
    print("Square root: ",math.sqrt(n))
    print("Logarithm: ",math.log(n))
    print("sine: ",math.sin(n))
except Exception as e:
    print(e)

