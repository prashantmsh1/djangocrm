import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="prashant",
)


cursorObject = db.cursor()

cursorObject.execute("CREATE DATABASE dcrm")
print("Database created")

# Ignore compiled Python files
*.pyc

# Ignore the virtual environment directory
venv/

# Ignore the IDE-specific files
.vscode/
.idea/

