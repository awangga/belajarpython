import csv
import sqlite3
import matplotlib.pyplot as plt
import requests

class Nuha(object):
    def __init__ (self, nama):
        self.nama = nama
    
    def peminjam(self):
        no_anggota = "112291"
        if(no_anggota)=="112291":
            print("Kiat Pintar Corel Draw")
        elif(no_anggota)=="112295":
            print("Psikologi Perusahaan")
        elif(no_anggota)=="112297":
            print("Cerdas Menguasai GIT")
        else:
            print("Anda Belum Meminjam Buku")

    def kategori(self):
        baris1 = "Kom"
        baris2 = "Psi"
        baris3 = "Bis"
        try:
            if baris1 == "Kom":
                print("Komputer")
            elif baris2 == "Psi":
                print("Psikolog")
            elif baris3 == "Bis":
                print("Bisnis")
            else:
                print("Kategori Lain")
        except Exception as a:
            print(a)
            print("cek ulang")

    def grafik(self):
        print("Ini Adalah Grafik Peminjaman Bukuuu Selama 1 tahun...")
        x = [1,2,3,4,5,6,7,8,9,10,11,12]
        y = [70,85,78,90,85,50,60,80,70,90,75,80]
        plt.plot(x,y)
        plt.xlabel('Bulan')
        plt.ylabel('Jumlah Peminjam')
        plt.title('Grafik Peminjaman Buku Perpustakaan 2019')
        plt.show()
        
    
    def database(self):
        koneksi = sqlite3.connect('kelas_2c/nuha.db')
        cursor = koneksi.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS \
                DATA_BUKU(KODE_BUKU INTEGER PRIMARY KEY, JUDUL TEXT, KATEGORI TEXT, STOK REAL)')
        tampil = "SELECT * FROM DATA_BUKU "
        try:
            cursor.execute("INSERT INTO DATA_BUKU VALUES(123,'Pintar Corel Draw', 'Komputer', 91)")
            koneksi.commit()
        except Exception:
            print("Record sudah ada")
        cursor.execute(tampil)
        results = cursor.fetchall()
        for row in results:
            kode_buku = row[0]
            judul = row[1]
            kategori = row[2]
            stok = row[3]
            print ("kode_buku %s, berjudul %s, dengan kategori %s, jumlah stok tersisa %s" % \
            (kode_buku, judul, kategori, stok))
    
    def baca_csv(self):
        with open('kelas_2c/data.csv','r') as data:
            reader = csv.reader(data)
            for row in reader:
                if str(row[0]) == self.nama:
                    print("Nama Peminjam", row[0], "meminjam dengan judul", row[2])

    def reques(self):
        req = requests.get('https://drakorindo.cc/drama-korea-romantic-doctor-teacher-kim-2-subtitle-indonesia/')
        req.encoding      
        req.status_code   
        req.elapsed       
        req.url           
        req.history  
        req.headers['Content-Type']
        try:
            print(req.status_code)
            print(req.encoding)
            print(req.headers)
            print(req.url)
            print(req.elapsed)
            print(req.history)
        except Exception as e:
            print(e)

    def buku_baru(self):
        kode_bukua= "1309"
        kode_bukub = "1209"
        kategoria= "Komputer"
        kategorib= "Bisnis"
        judula = "Arsitektur Komputer"
        judulb = "Memulai Bisnis Tanpa Modal"
        jumlah_bukbara = "15"
        jumlah_bukbarb = "10"
        tgl_masuk = "01-01-2020"

        if kode_bukua[1] =="3":
            print(kategoria,judula,jumlah_bukbara,tgl_masuk)
        elif kode_bukub[1] =="2":
            print(kategorib,judulb,jumlah_bukbarb,tgl_masuk)

    def ratapeminjam(self):
        print("Rata Rata-Rata Peminjam 1 tahun")
        nilaii = [79, 50, 55, 65, 80, 86, 68, 30, 49, 70, 82, 74]
        x = 1
        if x < 13 :
            try:
                print((nilaii[1] + nilaii[0] + nilaii[2]+ nilaii[3]+ nilaii[4]+ nilaii[5]+ nilaii[6]+ nilaii[7]+ nilaii[8]+ nilaii[9]+ nilaii[10]+ nilaii[11])/12)
            except Exception as e:
                print(e)

    def printrow(self):
        with open('kelas_2c/data.csv','r') as data:
            reader = csv.reader(data)
            for row in reader:
                print(row)

    def running(self):
        self.peminjam()
        self.kategori()
        self.grafik()
        self.database()
        self.baca_csv()
        self.reques()
        self.buku_baru()
        self.ratapeminjam()
        self.printrow()
