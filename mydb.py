import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = '@1210cheloti' 
	) 
# prepare a cursor object
cursorObject = dataBase.cursor()

# create the database

cursorObject.execute("CREATE DATABASE eldocore")
print("all done")