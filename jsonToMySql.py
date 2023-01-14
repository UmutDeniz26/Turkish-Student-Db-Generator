import mysql.connector
import json

sql = "INSERT INTO students_table (fname, lname, num, dept, pob, dob) VALUES ('%s', '%s', %s, %s, '%s', '%s')"
f=open('data.json','r',encoding='utf-8');

jsonDatabase=json.load(f)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pass",
  database="students"
)

for elements in jsonDatabase['students']:
  val=(elements['fname'],elements['lname'],str(elements['num']),elements['dept'],elements['pob'],str(elements['dob']))
  mycursor = mydb.cursor()
  mycursor.execute(sql %val)
  mydb.commit()


print(mycursor.rowcount, "record inserted.")