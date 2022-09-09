import sqlite3

conn=sqlite3.connect('SQL Database/SIH.db')

c=conn.cursor()
# c.execute("""CREATE TABLE student (
#             StudentName text,
#             StudentId text NOT NULL PRIMARY KEY,
#             Gender text,
#             Course text,
#             Department text,
#             Year text,
#             Semester text,
#             Mobile text,
#             Email text,
#             Photo text
#             )""")

c.execute("SELECT * from student")
# c.execute("DROP TABLE student")
items=c.fetchall()
print(items)

conn.commit()