import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET name = 'pashyo' WHERE name = 'pintu'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
