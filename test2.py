import sqlite3
MySchool=sqlite3.connect('schooltest.db')
curschool=MySchool.cursor()


for i in range(1,5):
    mysid=int(input("enter id:"))
    myname=input("enter name:")
    myage=int(input("enter age:"))
    mymarks=float(input("enter marks:"))
    curschool.execute("insert into student(StudentID,name,age,marks) values (?,?,?,?);",(mysid,myname,myage,mymarks))

MySchool.commit()



             
