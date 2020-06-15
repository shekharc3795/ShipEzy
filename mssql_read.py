import mysql.connector
from mysql.connector import Error
try:
    mydb =mysql.connector.connect(
        host="localhost",
        user="root",
        database = "shipezy",
        password = "Jain250218",
        )

    for x in range (1,100):
        id = x
        query2 = 'INSERT INTO shipezy.customer (cust_id, cust_name) VALUES (' +str(id)  +''Shekhar')'
    cursor.execute(query2)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

    query1 = "select * from shipezy.customer"
    cursor = mydb.cursor()
    cursor.execute(query1)
    records = cursor.fetchall()
    print("Total number of rows in user is: ", cursor.rowcount)
    for x in records:
        print(x)

    mycursor = mydb.cursor()

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (mydb.is_connected()):
        mydb.close()
        cursor.close()
        print("MySQL connection is closed")