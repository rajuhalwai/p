import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE name ='pintu' "

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")