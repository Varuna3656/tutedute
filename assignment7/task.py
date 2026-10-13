import psycopg2
def connection():
    conn = psycopg2.connect(dbname='postgres',user="postgres",password=251196,host='localhost',port="5432")
    
    cursor = conn.cursor()
    cursor.execute("drop table students;")
    cursor.execute("create table students(name text, rollNo int, DOB date, class text, comb text);")
    print("Table created succesfuly")

    conn.commit()
    conn.close()

def addData1():
    conn = psycopg2.connect(dbname='postgres',user="postgres",password=251196,host='localhost',port="5432")
    
    cursor = conn.cursor()
    cursor.execute("insert into students values('sameer',101,'2010-05-25', 'I PUC','EBAS');")
    cursor.execute("insert into students values('samanvi',102,'2011-09-22','I PUC','PCMC');")
    cursor.execute("insert into students values('ayush',103,'2011-04-05', 'I PUC', 'PCMC');")
    cursor.execute("insert into students values('shree lekha',104,'2012-10-14', 'I PUC', 'PCMB');")
    cursor.execute("insert into students values('Poorvika', 105,'2010-12-26', 'II PUC', 'PCMC');")

    print("Added multiple records succesfully")

    conn.commit()
    conn.close()
def extract():
    conn = psycopg2.connect(dbname='postgres',user="postgres",password=251196,host='localhost',port="5432")
    cursor = conn.cursor()
    cursor.execute("select * from students;")
    print("Printing all the data")
    print(cursor.fetchall())

    cursor.execute("select * from students where rollno=105;")
    print("Printing using where condition")
    print(cursor.fetchone())
    conn.commit()
    conn.close()


def delete():
    conn = psycopg2.connect(dbname='postgres',user="postgres",password=251196,host='localhost',port="5432")
    cursor = conn.cursor()
    cursor.execute("TRUNCATE table students;")

    print("Deleted records succesfully")

    conn.commit()
    conn.close()


def addData():
    conn = psycopg2.connect(dbname='postgres',user="postgres",password=251196,host='localhost',port="5432")
    cursor = conn.cursor()

    print("Please enter the details to add a student")
    name=input("Enter the name")
    rollno = int(input("Enter the id"))
    dob = input("Enter the DOB in YYYY-MM-DD format")
    cls=input("Enter the class")
    comb = input("Enter combination")


    query = "insert into students values(%s,%s, %s,%s,%s);"
    cursor.execute(query,(name,rollno,dob,cls,comb))
    print("Record added succesfully")
    
    conn.commit()
    conn.close()

connection()
addData1()
extract()
addData()
delete()