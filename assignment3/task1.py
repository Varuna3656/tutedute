def fact(n):
    if(n<=1):
        return n
    else:
        return n*fact(n-1)
try:
    n = int(input("Enter a number: "))
    result = fact(n)
    print(f"Factorail of {n} is {result}")
except Exception as e:
    print(e)