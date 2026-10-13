import psycopg2
def connection():
    conn = psycopg2.connect(dbname='postgres',user="postgres",password=251196,host='localhost',port="5432")
    
    cursor = conn.cursor()
    cursor.execute("create table employee(name text, ID int, age int);")

    conn.commit()
    conn.close()

def addData():
    conn = psycopg2.connect(dbname='postgres',user="postgres",password=251196,host='localhost',port="5432")
    
    cursor = conn.cursor()
    #cursor.execute("insert into employee values('sam',101,42);")
    cursor.execute("insert into employee values('sam',102,43);")
    conn.commit()
    conn.close()
#connection()
def extract():
    conn = psycopg2.connect(dbname='postgres',user="postgres",password=251196,host='localhost',port="5432")
    cursor = conn.cursor()
    cursor.execute("select * from employee;")
    print(cursor.fetchall())
    conn.commit()
    conn.close()


def delete():
    conn = psycopg2.connect(dbname='postgres',user="postgres",password=251196,host='localhost',port="5432")
    cursor = conn.cursor()
    cursor.execute("TRUNCATE table employee;")
    #print(cursor.fetchall())
    conn.commit()
    conn.close()


def addData():
    conn = psycopg2.connect(dbname='postgres',user="postgres",password=251196,host='localhost',port="5432")
    cursor = conn.cursor()

    name=input("Enter the name")
    id = int(input("Enter the id"))
    age = int(input("Enter the age"))

    query = "insert into employee values(%s,%s, %s);"
    cursor.execute(query,(name,id,age))
    
    conn.commit()
    conn.close()
#addData()
extract()
#delete()