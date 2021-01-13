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
	
	print('Database Connection Successfull')
	
	c.execute("INSERT INTO balances(Reg_No,First_Name,Second_Name,Section,Class,Term,Year,Balance) VALUES (?,?,?,?,?,?,?,?)",('ivan','23','male','developer','540',))
	c.commit()
	db.close()
		  


except Exception as e:
	print(e) #this prints out the error if there is any
	
	
#=============================inserting data in our database table=====================
