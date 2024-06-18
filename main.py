import sqlite3

con = sqlite3.connect('mahasiswa.db')
cur = con.cursor()

# Create & Insert
# cur.execute("CREATE TABLE mahasiswas (nim integer, name text, jurusan text, alamat text)")
# cur.execute("INSERT INTO mahasiswas VALUES (1002, 'Arta Windy', 'Manajemen Informatika', 'Lampung')")'

while True:

  InputNim = input("Masukkan NIM Anda: ")


  # Select
  mahasiswas = cur.execute(f"SELECT * FROM mahasiswas WHERE nim={InputNim}")
  mahasiswas = list(mahasiswas)
  if mahasiswas:
      for row in mahasiswas:
          nama = row[1]
          jurusan = row[2]
          print(f"Nama saya {nama}, dari jurusan {jurusan}")
  else:
      print("Mahasiswa dengan NIM tersebut tidak ditemukan.")
      print("Apakah ingin menambahkan mahasiswa? (Y/N)")
      tambah_mahasiswa = input().strip().upper()
      if tambah_mahasiswa == 'Y':
          nim_baru = input("Masukkan NIM: ")
          nama_baru = input("Masukkan Nama: ")
          jurusan_baru = input("Masukkan Jurusan: ")
          alamat_baru = input("Masukkan Alamat: ")
          try:
              cur.execute("INSERT INTO mahasiswas VALUES (?, ?, ?, ?)", (nim_baru, nama_baru, jurusan_baru, alamat_baru))
              print("Mahasiswa berhasil ditambahkan.")
          except sqlite3.Error as e:
              print("Gagal menambahkan mahasiswa:", e)

  con.commit()

  ulang = input("Apakah ingin melakukan pengecekan kembali? (Y/T): ")
  if ulang.upper() != 'Y':
      break




