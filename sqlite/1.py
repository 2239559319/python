import sqlite3

con=sqlite3.connect("D:\\sqlite\\test1.db")
cursor=con.cursor()
cursor.execute("select * from table1;")
print(cursor.fetchall())
cursor.execute('''update table1 set type="大学生" where name="xiaochuan";''')
con.commit()

con.close()