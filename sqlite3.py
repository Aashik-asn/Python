import sqlite3

conn=sqlite3.connect("sample")
cursor=conn.cursor()

cursor.execute("Create table IF not exists users(id int primary key,name char(30) Not null,age int not null)")


def display():
    cursor.execute("Select * from users")
    users=cursor.fetchall()
    if users:
        print("ALL RECORDS:")
        for row in users:
            print(row)
    else:
        print("No record found")

def insert():
    id1=int(input("Enter id: "))
    name=input("Enter name: ")
    age=int(input("Enter age: "))
    cursor.execute("Insert into users values(?,?,?)",(id1,name,age))
    conn.commit()

def delete():
    id1=int(input("Enter id to delete: "))
    cursor.execute("Delete from users where id=?",(id1,)) #(id1,) - tuple(singleton)
    conn.commit()

def update():
    id1=int(input("Enter id to make changes: "))
    age=int(input("Enter updated age: "))
    cursor.execute("update users set age = ? where id = ?",(age,id1))
    conn.commit()

while True:
    print("1. Insert")
    print("2. Display")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")
    flag=int(input("Enter no. 1/2/3/4: "))
    if flag==1:
        insert()
    elif flag==2:
        display()
    elif flag==3:
        update()
    elif flag==4:
        delete()
    elif flag==5:
        print("Exiting...")
        break
    else:
        print("Invalid entry")
conn.close()
