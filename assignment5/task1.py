students ={'Asha':95,'Babitha':89,'clarin':80,'derick':40}
try:
    name=input("Enter the student's name:")
    print(name,"'s marks:",students[name])
except KeyError:
    print("Student not found")