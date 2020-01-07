import csv
import sqlite3
import matplotlib.pyplot as plt
import requests

class Hitung:
   def Isi(self):
        self.f = open('kelas_2b/Etika.csv','r')
        self.reader = csv.reader(self.f)
        for row in self.reader:
            print ('Jumlah dari %s + %s adalah %s' %(row[0], row[1], float(row[0]) + float(row[1])))
        self.f.close()
   def koneksi_dan_buat(self):
        #mengkoneksikan database dan membuat database
        con = sqlite3.connect('data.db')
        #supaya tidak ada lagi akses dari database sehingga tidak proses jalan terus menerus
        con.close()
   def create_table(self):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        #execute fungsinya mengeksekusi perintah sql
        c.execute('create table if not exists  Mahasiswi(npm REAL, nama TEXT)')
        #create tabel if not exits artinya jika table sudah ada tidak perlu dibuat lagi
        conn.close()
   def insert_table(self):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        #perintah sql untuk insert data
        c.execute("INSERT INTO Mahasiswi VALUES(1184065,'Etika Khusnul Laeli')")
        conn.commit()
        c.close()
        conn.close()
   def read_data(self):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        #perintah sql untuk menampilkan data pada table
        c.execute('SELECT * FROM Mahasiswi')
        #perulangan untuk membuat data tampil semua
        for row in c.fetchall():
            print(row)
        c.close()
        conn.close()
   def update_data(self):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        #perintah sql untuk mengubah data
        c.execute("UPDATE Mahasiswi SET nama = 'Anif Nurrohman' WHERE npm = 1184095")
        conn.commit()
        c.close()
        conn.close()
   def delete_data(self):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        #perintah sql untuk menghapus data
        c.execute('DELETE FROM Mahasiswi WHERE npm = 1184065')
        conn.commit()
        c.close()
        conn.close()
   def gambar_garisputus(self):
        plt.plot([8,10,12,14,16,18,20],[40,60,98,80,98,80,60])
        plt.show()
   def show_gambargarisputus(self):
       plt.plot([8,10,12,14,16,18,20],[40,60,98,80,98,80,60], 'g--d')
       plt.show()
   def youtube_ReqGET(self):
        req = requests.get('https://www.youtube.com/channel/UCNBUPDfVtkVbSbsXtRZzVTw?view_as=subscriber')
        req.content
        req.status_code
        req.elapsed
        req.url
        req.history
        req.headers['Content-Type']
        #panggil
        print(req.content)
        print(req.status_code)
        print(req.elapsed)
        print(req.url)
        print(req.history)
        print(req.headers)
   def ReqPOST(self):
        req = requests.post('http://kampus.awangga.net/', data = {'search': 'assignments'})
        req.raise_for_status()
        req.url
        req.history
        #panggil
        print(req.raise_for_status)
        print(req.url)
        print(req.history)
   #menjalankan perintah
   def bismillah(self):
       self.koneksi_dan_buat()
       self.create_table()
       self.insert_table()
       self.read_data()
       print('row')
       self.update_data()
       self.delete_data()
       self.gambar_garisputus()
       self.show_gambargarisputus()
       self.youtube_ReqGET()
       self.ReqPOST()



