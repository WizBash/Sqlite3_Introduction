import sqlite3


try:

	db=sqlite3.connect('pass.db')
	conn=db.cursor()
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
	print(e)
