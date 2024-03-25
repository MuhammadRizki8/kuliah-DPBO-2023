import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_artis"
)

dbcursor = mydb.cursor()

sql = "INSERT INTO artis (nama_artis) VALUES (%s)"
val = ("Haji Sulam",)
dbcursor.execute(sql, val)
mydb.commit()

print(dbcursor.rowcount, "data inserted.")

dbcursor.execute("SELECT * FROM artis")
myresult = dbcursor.fetchall()

for x in myresult:
    print(x)

dbcursor = mydb.cursor()
sql = "DELETE FROM artis WHERE id_artis = '6'"
dbcursor.execute(sql)
mydb.commit()

print(dbcursor.rowcount, "data(s) deleted.")
