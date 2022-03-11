import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="latihandatabase1"
)

def insert_data(mydb):
    alternatif = input("alternatif : ")
    bobot = input("Bobot : ")
    peran = input("Peran : ")
 
    val = (alternatif, bobot, peran)

    cursor = mydb.cursor()

    sql = "INSERT INTO Alternatif (alternatif, bobot, peran) VALUES (%s, %s, %s)"
    
    cursor.execute(sql, val)
    mydb.commit()
    print("{} data berhasil disimpan". format(cursor.rowcount))

insert_data(mydb)