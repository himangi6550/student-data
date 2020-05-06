


import sqlite3
MySchool=sqlite3.connect('schooltest.db')
curschool=MySchool.cursor()
curschool.execute("select * from student where name=='Shelock' ;")


    
while True:
    record1=curschool.fetchone()
    if record1==None:
        break
    print (record1)

curschool.execute("select name from student where name=='Shelock' ;")
while True:
    record1=curschool.fetchone()
    if record1==None:
        break
    print (record1)
