'1.connect()'
'''
-In Python, .connect() is a method used to establish a connection between your Python program and a database.
 The exact syntax depends on the database library (such as SQLite, MySQL, or PostgreSQL).
 
-syntax
import database_module
connection = database_module.connect(parameters)

-What .connect() Returns
It returns a connection object, which is used to perform database operations.
cursor=conn.cursor()

'''
'1.1.we create connection establishment variable between python and database using connect()'
'''
-when we have connect python to database we need a connector variable 

'syntax in case of mysql"
connection_establisher_variable=database_connector_module_name.connect(
    host="host_name",
    username="username_of_database"
    password="password_of_database"
    database="database_name"
)'''
# eg
import mysql.connector 
conn=mysql.connector.connect(host="localhost",username="root",password="System",database="MySQL")
print(conn)
#<mysql.connector.connection_cext.CMySQLConnection object at 0x000001EE089956A0>


'2.cursor()'
'syntax'
'cursor_variable(stores returned object from database)=connection_establisher_variable.cursor()'
'''
-we use cursor in database programming because it acts as a bridge between 
python and the database to execute SQl commands and handle results
'''
#eg 
cursor=conn.cursor()



'3.execute()'
'syntax'
'cursor_variable_name.execute()'
''''
-execute() is defined inside the cursor class of database connector libraries
like mysql.connector(mysql connector for python) and sqlite3(sqlite in python)
-we use execute() to send SQL commands form python to the database, it tells 
the database --
      "Run this SQL query and return the result"
'''     
#eg
cursor.execute("use pydb")
cursor.execute("select * from student")
result1=cursor.fetchall()
print(result1)
# [(1, 'sam', 84), (2, 'krishana', 99), (3, 'parkar', 90), (4, 'vijay', 60)]




'4.Fetall()'
'syntax'
'variable_name(store returned object from database) = cursor_variable_name.fetchall()'

''
'''
-Fetall() is defined inside the cursor class of database connector libraries
like mysql.connector(mysql connector for python) and sqlite3(sqlite in python)
-we use fetchall() to retrive all row returned by a sql query at once , it is
mostly after executing a select query 
'''
#eg
cursor.execute("select * from employee")
result2=cursor.fetchall()
print(result2)
# [(1, 'sam', 84000), (2, 'krishana', 90009), (3, 'parkar', 90000), (4, 'vijay', 60000)]



'5.commit()'
'syntax'
'connection_establish_variable_name.commit()' # here variable is connection Establisher
'eg - conn.commit()'

'let this function understand by question'
'''
Q1.why we use conn.commit() when executing INSERT,UPDATE and DELETE queries
 in python to malkw the changes permanent in the database'''
 
'''Ans
-we use conn.commmit() in python database programming because most of database
drivers's (like mysql.connector , psycopq2,sqlite3,...etc) run in the transaction
mode by default
-meaning of above statement 
when you execute INSERT , UPDATE or DELETE , the changes are not immediately
saved permanently in the  database, instead they are kept in a temporary 
transaction buffer

Q2.Why conn.commmit() is needed 
Ans :
a.make changes permant in the database 
b.save (commmit) the current transaction 
c.Ensure that INSERT/UPDATE/DELETE operations are actually applied

Q3.What happens without commit ()?
Ans:
a.changes remain temporary
b.they may be rolled back automatically when 
   i)the program ends
   ii)conn.rollback() is called 
   iii)the connections is closed(in some DB setups)
c.so your data may apper updated in the program but will not stored in the database   
'''
#eg
cursor.execute("update student set sname = 'shubham' where id = 4") 
conn.commit()
cursor.execute("select * from student")
result3=cursor.fetchall()
print(result3)
# [(1, 'sam', 84), (2, 'krishana', 99), (3, 'parkar', 90), (4, 'shubham', 60)]
'''
NOTEs:connection_establish_variable.commit() used in case  of table data like INSERT , UPDATE , DELETE method 
but it does not require in case of table structure like drop table , drop databse ,  alter table --> reanme, modify column datatype , add column , drop column ,

'''

