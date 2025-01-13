import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost", user = "root", password = "W7301@jqir#"
)

# print(mydb)
mycursor = mydb.cursor()
mycursor.execute("Create database Library_Management_System")
