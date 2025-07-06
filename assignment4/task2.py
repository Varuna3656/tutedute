try:
    fo = open("assignment4\output.txt","a+")
    print("Enter text to write to the file:")
    data = input()
    count=fo.write(data+"\n")
    if count:
        print("data successfully written to output.txt")
    print("Enter additonal text to append:")
    data=input()
    fo.write(data+"\n")
    fo.seek(0)
    print("Final content of output.txt",end=":\n")
    content =fo.read()
    print(content)    
except Exception as e:
    print(e)
