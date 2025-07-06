try:
    num = int(input("Enter a number: "))
    if(num%2==0):
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")
except ValueError:
    print("Enter only integer values")