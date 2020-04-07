import mysql.connector


db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="inventaris"
)





def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM data_inventaris"
    cursor.execute(sql)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)





def show_menu(db):
  print("=== APLIKASI INVENTARIS ===")
  print("1. Insert Data")
  print("------------------")
  menu = input("Pilih menu> ")


  if menu == "1":
    show_data(db)
  else:
    print("Menu salah!")

if __name__ == "__main__":
    while (True):
        show_menu(db)

