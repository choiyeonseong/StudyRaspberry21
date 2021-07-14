import MySQLdb

# (ip or domain, userid, password, database)
db = MySQLdb.connect('localhost', 'root', '12345', 'test', charset='utf8')

cur=db.cursor(MySQLdb.cursors.DictCursor)

# insert
cur.execute("insert into student values ({0}, '{1}','{2}')".format(3, 'FullName', '1987-06-24'))
db.commit() # commit

# select
cur.execute('SELECT * FROM student')

while True:
    student=cur.fetchone()
    if not student: break

    print(student)

cur.close()
db.close()