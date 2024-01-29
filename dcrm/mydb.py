import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="prashant",
)


cursorObject = db.cursor()

cursorObject.execute("CREATE DATABASE dcrm")
print("Database created")
