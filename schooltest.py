import sqlite3
MySchool=sqlite3.connect('schooltest.db')
nm=input("enter name:")
sql="select*from student where name= '"+nm+"';"
curschool=MySchool.cursor()
curschool.execute(sql)
record =curschool.fetchone()
print(record)

res=input("do you want to delete this record?(Y/N)")
sql="delete from student where name='"+nm+"';"
if res=='Y':
    try:
        curschool.execute(sql)
        MySchool.commit()
        print("record deleted successfully")
    except:
        print("error in update operation")
        MySchool.rollback()
MySchool.close() 
