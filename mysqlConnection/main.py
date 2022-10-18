import mysql.connector
mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "test"
)
mycursor = mydb.cursor()
name = input("Please Enter Name: ")
age = input("Please Enter Age: ")
sql = "INSERT INTO user (name, age) VALUES (%s, %s)"
val = (name,age)
mycursor.execute(sql,val)

mycursor.execute("select * from user")
print(mycursor.fetchall())
mydb.commit()
print(f"{mycursor.rowcount} is added")

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="test"
# )
#
# mycursor = mydb.cursor()
#
# name = input("Please Enter Name: ")
# age = input("Please Enter Age: ")
# sql = "INSERT INTO user (name, age) VALUES (%s, %s)"
# val = (name,age)
#
# mycursor.execute(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "record inserted.")

