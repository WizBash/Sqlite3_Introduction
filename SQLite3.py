#===============================WE FIRST IMPORT THE SQLITE3 MODULE ================
import sqlite3

#======================== WE USE TRY TO RAISE ERRORS INCASE THERE IS ANY======================
try:
	#========================creating and connecting to our databse====================
	db=sqlite3.connect('pass.db')
	conn=db.cursor()
	
	#===============================creating table in our databse=====================
	conn.execute("""CREATE TABLE IF NOT EXISTS pass_table (
	NAME TEXT,
	AGE INT,
	SEX TEXT, 
	JOB TEXT,
	SALARY INT 
	)
	""")
	db.commit()
	db.close()
	print('Database Connection Successfull')

except Exception as e:
	print(e) #this prints out the error if there is any
	
	
#=============================inserting data in our database table=====================
