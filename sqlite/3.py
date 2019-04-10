#sqlite站位符的使用
import sqlite3

con=sqlite3.connect("test.db")
c=con.cursor()
name="小川"
c.execute("select * from table1 where name='%s'"%name)
print(c.fetchone())
c.execute("select * from table1 where name=?",(name,))#放置?作为占位符，只要您想要使用值，然后提供一个元组值作为光标的execute()方法的第二个参数。
print(c.fetchone())