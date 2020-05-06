import sqlite3
MySchool=sqlite3.connect('schooltest.db')
curschool=MySchool.cursor()
curschool.execute("select * from student where StudentID==10;")

result=curschool.fetchall()
for record in result:
    print(record)
