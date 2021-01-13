#===============================WE FIRST IMPORT THE SQLITE3 MODULE ================
import sqlite3

#======================== WE USE TRY TO RAISE ERRORS INCASE THERE IS ANY======================
try:
	#========================creating and connecting to our databse====================
	db=sqlite3.connect('Informtaion.db')
	conn=db.cursor()
	
	#===============================creating table in our databse=====================
	conn.execute("""CREATE TABLE IF NOT EXISTS info_table (
	NAME TEXT,
	AGE INT,
	SEX TEXT, 
	JOB TEXT,
	SALARY INT 
	)
	""")
	db.commit()
	
	print('Database Connection Successfull')
	
	#=============================inserting data in our database table=====================
	c.execute("INSERT INTO info_table(NAME,AGE,SEX,JOB,SALARY,) VALUES (?,?,?,?,?,?,?,?)",('ivan','23','male','developer','540',))
	c.commit()
	db.close()
		  


except Exception as e:
	print(e) #this prints out the error if there is any
	
	

