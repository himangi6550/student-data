import sqlite3
MySchool=sqlite3.connect('schooltest.db')
curschool=MySchool.cursor()


sql="INSERT INTO student(StudentID, name, age , marks) VALUES (?,?,?,?);"

val= [ (129,'Pride and Prejudice',12,190),
       (126,'Sherlock Holmes',23,270),
       (187,'War And Peace',23,700),
       (149,'David Copperfield',42,300),
       (194,'Half Girlfriend',34,170),
        ]
curschool.executemany("INSERT INTO student(StudentID, name, age , marks) VALUES (?,?,?,?);",val)


MySchool.commit()
