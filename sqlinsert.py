# Import Python Modules
import random
import mysql.connector

from mysql.connector import Error

# Define Global Variables
sql_table1 = "shipezy.customer"

# Function for connecting, opening, committing and closing the database and executing the query string
def connect_mysql(query):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="shipezy",
            password="Jain250218",
            )
        cursor.execute(query)
        mydb.commit()
    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (mydb.is_connected()):
            mydb.close()
            cursor.close()
            print("MySQL connection is closed")
# Function for defining SQL select statement query string
def sql_select(sql_table):
    query_string = "SELECT * FROM  " + str(sql_table)
    return query_string
# Function for defining SQL insert statement query string
def sql_insert(sql_table, cust_id, cust_name):
    query_string = "INSERT INTO " + sql_table + "(cust_id, cust_name)" + "VALUE(" + cust_id +"," + cust_name+")"
    return query_string
# Creating a string to pass to MySQL database and updating the global table
for x in range (1,100):
        cust_name_ref = "s"+str(random.randint(0,1000))+"@gmail.com"
        sql_insert(sql_table1,str(x), cust_name_ref)
        connect_mysql(query_string)
# Reading the table about number of records updated
sql_select(sql_table)
connect_mysql(query_string)
cursor = mydb.cursor()
cursor.execute(query)
records = cursor.fetchall()
print("Total number of rows in user is: ", cursor.rowcount)
