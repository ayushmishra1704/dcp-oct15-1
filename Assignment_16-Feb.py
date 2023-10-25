""" Q.1. Database is a collection of related information that can be stored. Information can be structured(in rows and columns) or unstructured(in json format).
e.g. grocery shopping list. 

SQL Database can only store structured format data whereas Not Only SQL Database can store non-structured format data.
Some e.g of Structured Database are MySql, Postgre SQL where e.g. of Not Only SQL Database are MongoDB, Cassandra.
Data in SQL Database is stored in rows and columns in tables whereas Data in NO SQL Database is stored in in anthing but a traditional table.
Some e.g of structured data format is csv whereas e.g of unstructured data format is json.

Q.2. Data Definition Language - We define database schema in DDL. Database schema is all different tables and relations that database is going to store.
CREATE - It is a keyword which is used to create database and tables.
ALTER - It is a keyword which is used to modify the structure of database table (add, delete columns in a table or add, delete keys, indexes in a table or change the type in a specific column).
DROP - It is a keyword which is used to drop the table or any column in a table when the table is not needed or drop it accoding to different situations.
"""
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = "password"
)

my_cursor = mydb.cursor()
my_cursor.execute("CREATE DATABASE if not exists database4")
my_cursor.execute("CREATE TABLE if not exists database4.student(Name VARCHAR(15), Subject_Name VARCHAR(15))")
my_cursor.execute("ALTER TABLE database4.student ADD gpa DECIMAL(3,2)")
my_cursor.execute("ALTER TABLE database4.student DROP COLUMN gpa")
my_cursor.execute("SELECT * FROM database4.student")
for i in my_cursor.fetchall():
    print(i)


"""TRUNCATE - It is keyword which is used to delete all the rows from a table regqardless of whether conditions are metor not. """
my_cursor.execute("TRUNCATE TABLE database4.student")


"""
Data Manipulation Language- It is used to insert, update or delete the data in database table or simply it is used to maniplate data in after schema is defined.
INSERT - It is a keyword which is used to insert the new data in the table of the database.
UPDATE - It is a keyword which is used to update the existing data in the row of table for a particular column or multiple columns.
DELETE - It is used to delete the data in the table(entire row, multiple rows ).
"""
my_cursor.execute("CREATE DATABASE if not exists database6")
my_cursor.execute("CREATE TABLE if not exists database6.studentnit(Name VARCHAR(15) PRIMARY KEY, Subject_Name VARCHAR(15))")
my_cursor.execute("INSERT INTO database6.studentnit VALUES('Ayush', 'Maths')")
my_cursor.execute("INSERT INTO database6.studentnit VALUES('Vikas', 'Science')")
my_cursor.execute("INSERT INTO database6.studentnit VALUES('Vikas', 'Science')")
my_cursor.execute("UPDATE database6.studentnit SET Name = 'Nihar' WHERE Name = 'Vikas' ")
my_cursor.execute("DELETE FROM database6.studentnit WHERE Subject_Name = 'Maths' ")

"""Q.3. Data Query Language(DQL) - It is used to query the data in the database so that user can retrieve the relevant information from the database.
SELECT - It is used to retrieve the information in tabular form from a database
"""
my_cursor.execute("SELECT * FROM database6.studentnit")


"""Q.5. Primary Key -> It is an attribute which is used to uniquely identify each specific row. 
A particular column is generally declared a primary key if its each element corresponding to that particular row is unique.
Primary key can be string or numbers. There can be 2 or more primary key which forms a composite key because sometimes a particular column cannot alone define a primary key.
"""

my_cursor_execute("ALTER TABLE database6.studentnit ADD PRIMARY KEY(Name) ")


"""
Foreign Key -> It is an attribute which is used to connect a table of a database from another table.
"""
my_cursor_execute("ALTER TABLE database6.studentnit ADD FOREIGN KEY(Name) REFERENCES student(Name)")
mydb.close()

"""Q.6.
cursor() - It allows python code to execute sql commands in a database session. All comands are executed in the context of a database session wrapped by the session.
"""
import mysql.connector
mydb = mysql.connector.connect(
host = "localhost",
user = "abc",
password = "password"
)
my_cursor = mydb.cursor()
my_cursor.execute("CREATE DATABASE if not exists database5")
mydb.close()

"""
Q.7. 
There are 7 stages of  sql order of execution :
1. FROM - It is used with DQL statement SELECT to get data "FROM" a particular table.
2. WHERE  - It is used to filter records. It is also used in DQL statements to specify a particular condition in order to retrieve the data.
3. GROUP BY - The GROUP BY statement groups rows that have the same values into summary rows.
4. HAVING - The HAVING clause was added to sql because the WHERE keyword cannot be used with aggregate functions.
5. SELECT - It is used to retrieve the information in tabular form from a database. 
6. ORDER BY - It is used to sort the result set in ascending or descending order.
7. LIMIT - It is used in condition when only specific number of rows are required.
"""