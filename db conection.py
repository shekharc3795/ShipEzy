import mysql.connector
mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    database = "shipezy",
    password = "Jain250218",
    )
print(mydb)