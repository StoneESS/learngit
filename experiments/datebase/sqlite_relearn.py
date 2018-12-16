import sqlite3

data = dict([("id0%i"%x,dict([("name","name0%i"%x),("age",x)])) for x in range(1,5)])
data['id_test'] = {"name":666, "age":666}



conn = sqlite3.connect(":memory:")
conn.row_factory = sqlite3.Row
cur = conn.cursor()

cur.execute("create table user(name, age)")

for kw in data:
    cur.execute("insert into user(name, age) values(:name, :age)", data[kw])

#cur.execute("select name,age from user WHERE name=age")
cur.execute("select * from user")

rslt = cur.fetchone()
