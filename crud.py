import mysql.connector
import datetime
import re

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="inventaris"
)

# if db.is_connected():
#     print("suskses konek")


def insert_data(db):
    cur = db.cursor()
    sql = "INSERT INTO data_inventaris (inventaris_no, inventaris_nama, inventaris_jenis, inventaris_tglmasuk) VALUES (%s, %s, %s, %s)"

    nama = input("Masukan nama: ")
    jenis = input("Masukan jenis (LAMA/CEPAT): ")
    tgl = input("Masukan tgl (dd/mm/Y): ")

    tgl_formated = datetime.datetime.strptime(tgl, '%d/%m/%Y')

    sql_count_data = "SELECT COUNT(*) FROM data_inventaris WHERE inventaris_jenis ='" + jenis + "'"
    cur.execute(sql_count_data)
    jumlah_data = cur.fetchone()[0]


    if(jenis == 'LAMA'):

        if(jumlah_data != 0):
            last_data = "select *from data_inventaris WHERE inventaris_jenis = '" + jenis + "' ORDER BY inventaris_no DESC LIMIT 1"
            cur.execute(last_data)
            last_inven = cur.fetchone()[0]

            getlist = (re.findall('\d+', last_inven))
            no_urut = int(getlist[-1]) + 1

            no_inven = "LBI.1."+str(no_urut)+""

            val = (no_inven, nama, jenis, tgl_formated)
            cur.execute(sql, val)
            db.commit()
            print("{} data berhasil disimpan".format(cur.rowcount))

        else:
            no_inven = "LBI.1.1"
            val = (no_inven, nama, jenis, tgl_formated)
            cur.execute(sql, val)
            db.commit()
            print("{} data berhasil disimpan".format(cur.rowcount))



    elif(jenis == 'CEPAT'):
        if(jumlah_data != 0):
            last_data = "select *from data_inventaris WHERE inventaris_jenis = '" + jenis + "' ORDER BY inventaris_no DESC LIMIT 1"
            cur.execute(last_data)
            last_inven = cur.fetchone()[0]

            getlist = (re.findall('\d+', last_inven))
            no_urut = int(getlist[-1]) + 1

            no_inven = "LBI.2."+str(no_urut)+""

            val = (no_inven, nama, jenis, tgl_formated)
            cur.execute(sql, val)
            db.commit()
            print("{} data berhasil disimpan".format(cur.rowcount))

        else:
            no_inven = "LBI.2.1"
            val = (no_inven, nama, jenis, tgl_formated)
            cur.execute(sql, val)
            db.commit()
            print("{} data berhasil disimpan".format(cur.rowcount))

    else:
        print("Data tidak sesuai cek lagi !")


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


def update_data(db):
  cur = db.cursor()
  show_data(db)
  no_invent = input("Pilih No Inven> ")
  nama = input("Nama baru: ")

  sql = "UPDATE data_inventaris SET inventaris_nama=%s WHERE inventaris_no=%s"
  val = (nama, no_invent)
  cur.execute(sql, val)
  db.commit()
  print("{} data berhasil diubah".format(cur.rowcount))


def delete_data(db):
  cur = db.cursor()
  show_data(db)
  no_inven = input("Pilih No Inventaris>")
  sql = "DELETE FROM data_inventaris WHERE inventaris_no=%s"
  val = (no_inven,)
  cur.execute(sql, val)
  db.commit()
  print("{} data berhasil dihapus".format(cur.rowcount))



def show_menu(db):
  print("=== APLIKASI INVENTARIS ===")
  print("1. Insert Data")
  print("2. Tampilkan Data")
  print("3. Update Data")
  print("4. Hapus Data")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")


  if menu == "1":
    insert_data(db)
  elif menu == "2":
    show_data(db)
  elif menu == "3":
    update_data(db)
  elif menu == "4":
    delete_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")

if __name__ == "__main__":
    while (True):
        show_menu(db)

