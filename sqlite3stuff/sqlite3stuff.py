#Lessons learned from this stupid messy experminatation project:
#1. python comments suck.
#2. sqlite3 sucks and does not support multiple user access.  So my code was fine but it didn't seem like it was GR. STOOPID SQLITE LALALA.
#3. because sqlite 3 sucks, that funny comic about databases is valid.
#4. LALALALLALALALALALALALALLALALAAAAAAAAAAAAAAA
#5. I've been on lots of pain meds today.  TEHEEE!


import sqlite3

#create a db or connect to it, create table
#with sqlite3.connect('pokie.db') as db:
#    cursor = db.cursor()
#    sql = """create table Testing (
#    ObjectID integer
#    Name text
#    Cost real
#    Primary Key);"""
#    cursor.execute(sql)
#    db.commit()

conn = sqlite3.connect('pokie.db')
c = conn.cursor()
c.execute('''CREATE TABLE testing2 (name text, cost real)''')
val = ("halo", 42)
c.execute("INSERT INTO testing2 VALUES (?,?)", val)
conn.commit()
conn.close()

#insert some values... the dumb way
#values = ("hi there", 22)
#def insert_values(data):
#    with sqlite3.connect('pokie.db') as db:
#        cursor = db.cursor()
#        sql = "insert into Testing (Name, Cost) values (?,?)"
 #       cursor.execute(sql, data)
 #       db.commit()
#insert_values(values)