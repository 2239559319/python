import pymysql

con=pymysql.connect(host="localhost",user="root",password="2239559319",db="world")
cursor=con.cursor()
cursor.execute("select id from city")
datas=cursor.fetchall()
for data in datas:
    print(data[0])