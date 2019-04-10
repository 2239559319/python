#你可以把游标cursor 当做是一个迭代器，通过调用游标的fetchone()方法来获取单行结果；或者通过调用fetchall()方法获取结果集列表
import sqlite3

con=sqlite3.connect("test.db")
c=con.cursor()

for row in c.execute("select * from table1"):
    print(row)

c.close()
con.close()