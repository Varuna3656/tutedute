import io
try:    
    fo = open("assignment4\sample.txt",'r')
    content = fo.readlines()
    print("Reading file content:\n")
    i=1
    for l in content:
        print(f"Line {i}:",l)
        i+=1
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")