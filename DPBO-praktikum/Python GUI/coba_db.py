import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_toko_baju_tp3",
)

dbcursor = mydb.cursor()

sql_insert_kategori = "INSERT INTO kategori (nama_kategori) VALUES (%s)"
val_kategori = ("Pakaian Pria",)  # Add a comma after the string
dbcursor.execute(sql_insert_kategori, val_kategori)
mydb.commit()
print(dbcursor.rowcount, "kategori inserted.")

dbcursor.execute("SELECT * FROM kategori")
myresult=dbcursor.fetchall()
for x in myresult:
    print(x)

sql_delete_kategori = "DELETE FROM kategori WHERE nama_kategori = %s"
val_delete_kategori = ("Pakaian Pria",)
dbcursor.execute(sql_delete_kategori, val_delete_kategori)
mydb.commit()
print(dbcursor.rowcount, "kategori deleted.")

print("\nSetelah delete :")
dbcursor.execute("SELECT * FROM kategori")
myresult=dbcursor.fetchall()
for x in myresult:
    print(x)
