import mysql.connector
import time

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  port=3308
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO `remindDB`.`users` (`firstName`, `lastName`, `email`) VALUES ('John', 'Doe', 'email@example.com');")



time.sleep(10)

mycursor.execute("SELECT * FROM `remindDB`.`users`")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)