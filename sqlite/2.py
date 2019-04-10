import sqlite3

con=sqlite3.connect("test.db")
c=con.cursor()
c.execute('''create table table1
              (name text,
              age int )''')

c.execute("insert into table1(name,age) values('小川',21)")
c.execute("insert into table1(name,age) values('吕佳薪',20)")
con.commit()

c.execute("select * from table1")
print(c.fetchall())

c.close()
con.close()