'A.Database connectivity'


'-In this session we must have knowledge about MySQL Quaries '
'''
-Database connectivity in python is the proccess of connecting a python
application to a database to store , retrieve , update and manage data
efficiently
-When we have to connect python to any database we need connector  


#eg 
-in case of mysql database we need mysql.connector module
-if this module not available then python raise ModuleNotFoundError
-we have to install here mysql connector to connect mysql database


-processs of install mysql connector
1.Entre 
window + R
2.type cmd - run
cmd - write -  pip list (here cmd will show all installed libraries)
3.if module is not in list then install this way
cmd - pip install module_name   
#eg pip install mysql-connector-python 
4.again check 
cmd- pip list  '''


'''
NOTEs - To learn commit(), .fetchall() .execute() This concepts are metioned in session S42'''



# after installing connector follow the proccess below 

'1.Establishing a connection between python and mysql'
import mysql.connector
conn=mysql.connector.connect(host="localhost",username="root",password="System",database="MySQL")

print(conn)
#<mysql.connector.connection_cext.CMySQLConnection object at 0x000001FD0C1E9400>

'2.Creating a Cursor object to Execute SQL queries on the database connection'
cursor=conn.cursor()


'B.Database management using python '


'3.Create new database '
'''
cursor.execute("create database pydb")
print("New pydb database created successfully")
'''
#New pydb database created successfully

'''
4.Displaying list of already existing databases and also
verifying if newly created database get successfully created or not'''
cursor.execute("show databases")
result=cursor.fetchall()
print(result)
# #[('afternoon_db',), ('allweatherdb',), ('autumn',), ('clause_db',), ('college',), ('pydb',),]

'5.Use created database or switch database'
cursor.execute("use pydb")
print("Database switched successfully")
#Database switched successfully

'6.Creating new table in pydb database'
'''cursor.execute("create table student(id int , sname varchar(50),smarks int)")'''
print("student table get successfully created inside the pydb database")
# student table get successfully created inside the pydb database

'7.Displaying structure of student table'
cursor.execute("describe student")
result2=cursor.fetchall() 
print(result2)
#[('id', 'int', 'YES', '', None, ''), ('sname', 'varchar(50)', 'YES', '', None, ''), ('smarks', 'int', 'YES', '', None, '')]

'8.Inserting a Single row in a table'
'''cursor.execute("insert into student values(1,'ramananajun',95)") '''
conn.commit() # we use commit() to save changes permanently in the database 
print("A single inserted successfully into the student table")
#A single inserted successfully into the student table

'9.Inseerting multiple row in a table'
'''cursor.execute("insert into student (id , sname,smarks) values(2,'sam',84),(3,'krishna',99),(4,'shubham',85)")'''
'conn.commit()'
print("Multiple rows are inserted successfully into a table")
# Multiple rows are inserted successfully into a table

'10.displaying Entire data at a time from table'
cursor.execute("select * from student")
result3=cursor.fetchall()
print(result3)
#[(1, 'ramananajun', 95), (2, 'sam', 84), (3, 'krishna', 99), (4, 'shubham', 85)]

'11.creating another table '
'''
cursor.execute("create table employee(id int, ename varchar(50),esalary int)")
print("New table created successfully")'''
# New table created successfully
'''
cursor.execute("insert into employee (id , ename,esalary) values(1,'thomas',45000),(2,'alex',40000)")
conn.commit()
print("Multiple rows inserted successfully into the table ")'''
# Multiple rows inserted successfully into the table 

'''
12.displaying list of already existing tables in a database and also verifying if newly created table got successfully created or not '''

cursor.execute("show tables")
result4=cursor.fetchall()
print(result4)
#[('employee',), ('student',)]


'13.displaying entie data only from a specific column of a table '
cursor.execute("select sname from student")
result5=cursor.fetchall()
print(result5)
# [('ramananajun',), ('sam',), ('krishna',), ('shubham',)]

'14.displaying entire data from mutliple column of a table'

cursor.execute ("select sname, smarks from student")
result6=cursor.fetchall()
print(result6)
#[('ramananajun', 95), ('sam', 84), ('krishna', 99), ('shubham', 85)]

'15.displaying specific row of table'
cursor.execute("select * from student where smarks=99")
result7=cursor.fetchall()
print(result7)
#[(3, 'krishna', 99)]

'16.displaying multiple row from a table '
cursor.execute("select * from student where id>1 and id <4")
result8=cursor.fetchall()
print(result8)
#[(2, 'sam', 84), (3, 'krishna', 99)]

'17.Updating a specific value in a specific row of a table '
cursor.execute("update student set sname ='peter' where id = 4")
conn.commit()
print("Updated a specific value in a specific row of a table successfully")
# Updated a specific value in a specific row of a table successfully

''' from mysql command Line client 
mysql> select * from student;
+------+-------------+--------+
| id   | sname       | smarks |
+------+-------------+--------+
|    1 | ramananajun |     95 |
|    2 | sam         |     84 |
|    3 | krishna     |     99 |
|    4 | peter       |     85 |  # here our update value - shubham --> peter
+------+-------------+--------+
4 rows in set (0.00 sec)'''

'18.Upadating an entire specific row of a table'
cursor.execute("update student set id=5,sname='parker',smarks=100 where id =4")
conn.commit()
print("Updated entire row of a table")
#Updated entire row of a table

'''from MySQl command line client
mysql> select * from student;
+------+-------------+--------+
| id   | sname       | smarks |
+------+-------------+--------+
|    1 | ramananajun |     95 |
|    2 | sam         |     84 |
|    3 | krishna     |     99 |
|    5 | parker      |    100 | # here updated entire row of a table . for example look id is now 5
+------+-------------+--------+
4 rows in set (0.00 sec)'''

'19.renaming a table using alter table statement '
'''
cursor.execute("alter table std rename to student")
print("renamed a table successfully")'''
#renamed a table successfully 

'20.To check table renamed or not'
cursor.execute("show tables")
result9=cursor.fetchall()
print(result9)
#[('employee',), ('std',)]

'21.dropping specific column from table using alter table stmt'
'''
cursor.execute("alter table employee drop column esalary")
print("dropped specific column from a table successfully")'''
# dropped specific column from a table successfully

'22.adding a new column to an existing table using alter table stmt '
'''
cursor.execute("alter table employee add column edept varchar(50)")
print("added new column to an exist table successfully")'''
#added new column to an exist table successfully

'23.To verify new column add or not into existing table'
cursor.execute("select edept from employee")
result10=cursor.fetchall()
print(result10)
#[(None,), (None,)]
''' from MySQl command line client
mysql> select edept from employee;
+-------+
| edept |
+-------+
| NULL  |
| NULL  |
+-------+
2 rows in set (0.00 sec)'''

'24.Modifying the datatype of specific column in a table using the alter stmet'
'''
cursor.execute("alter table employee modify column id bigint")
print("modified the datatype of a specific column in table successfully")'''
# modified the datatype of a specific column in table successfully
'''
before 

from MySQl command line client
mysql> desc employee;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int         | YES  |     | NULL    |       |
| ename | varchar(50) | YES  |     | NULL    |       |
| edept | varchar(50) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
3 rows in set (0.00 sec)

after 
mysql> desc employee;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | bigint      | YES  |     | NULL    |       | # HERE we modified id column datatype int into bigint
| ename | varchar(50) | YES  |     | NULL    |       |
| edept | varchar(50) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
3 rows in set (0.00 sec)'''

'25.deleting a specific row from table using the delete stmt'
'''
cursor.execute("delete from student where id = 5")
conn.commit()
print("deleted a specific row from a table successfully")'''
#deleted a specific row from a table successfully

'26.Deleting entire data from a table using delete from stmt'
'''
cursor.execute("delete from student")
conn.commit()
print("delete entire data from a table successfully")'''
#delete entire date from a table successfully

'27.Droping specific table using drop table stmt '
'''
cursor.execute("drop table student")
print("dropped a specific table ")'''
#dropped a specific table 

'28.dropping a specific database using drop database stmt'
'''
cursor.execute("drop database pydb")
print("dropped a specific database successfully")'''
#dropped a specific database successfully



