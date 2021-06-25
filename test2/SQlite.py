import sqlite3
coon = sqlite3.connect('test.db')
cur = coon.cursor()
cur.execute("CREATE TABLE demo(num int,str varchar(20));")

cur.execute("INSERT INTO demo VALUES(%d,'%s')" % (1, 'aaa'))
cur.execute("INSERT INTO demo VALUES(%d,'%s')" % (2, 'bbb'))
cur.execute("INSERT INTO demo VALUES(%d,'%s')" % (3, 'ccc'))

cur.execute("UPDATE demo SET str='%S'WHERER num = %d" % ('ddd', 3))
cur.execute("SELECT * FROM demo;")
rows = cur.fetchall()
print('记录个数： %d'% len(rows))
for i in rows:
    print(i)

coon.commit()

cur.close()

coon.close()
