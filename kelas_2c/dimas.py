import sqlite3
import csv
import matplotlib.pyplot as plt
import requests

class maulana:
    def welcome(self):
        print ("Terimakasih telah menggunakan layanan kami, silakan pilih sesuai kebutuhan anda.")
        
    def ojek(self):
            with open('kelas_2c/ojek.csv', 'r') as csvfile:
                readCSV = csv.reader(csvfile)
                harga = []
                tujuan = []
                for row in readCSV:
                    tujuansaya = row[0]
                    hargaojek = row[1]
                    print(row[0], row[1])

            harga.append(hargaojek)
            tujuan.append(tujuansaya)
    
    def mpl(self):
        plt.plot([4,8,12,16,20],[40, 54, 68, 82, 96])
        plt.show()
        
    def request(self):
        req = requests.get('https://www.kaskus.co.id/')
        req.encoding      
        req.status_code   
        req.elapsed       
        req.url           
        req.history       
        req.headers['Content-Type']
        
    def database(self):
        sqlite3.connect('transport.db')
        print("Database berhasil dibikin")
        
    def tabel(self):
        db = sqlite3.connect('transport.db')
        cursor = db.cursor()
        sql = """CREATE TABLE kendaraan (
        jenis VARCHAR(30),
        layanan VARCHAR(30),
        tujuan VARCHAR(30)
        )"""
        cursor.execute(sql)
        print("Tabel transport berhasil dibuat!")
        
    def insert(self):
        db = sqlite3.connect('transport.db' )
        cursor = db.cursor()
        sql = """INSERT INTO kendaraan(jenis, layanan, tujuan)
        VALUES ('motor', 'grab', 'kampung rambutan')"""
        cursor.execute(sql)
        db.commit()
        print("{} data berhasil ditambahkan ke tabel".format(cursor.rowcount))
    
       
    def show(self):
        db = sqlite3.connect('transport.db')
        cursor = db.cursor()
        sql = "SELECT * FROM kendaraan"
        cursor.execute(sql)
        results = cursor.fetchall()
        for data in results:
            print(data)
            
    def delete(self):
        db = sqlite3.connect('transport.db')
        cursor = db.cursor()
        cursor.execute('DELETE FROM kendaraan WHERE layanan="grab"')
        db.commit()
        print("{} data dihapus dari tabel".format(cursor.rowcount))
        
    def together(self):
        self.welcome()
        self.ojek()
        self.mpl()
        self.request()
        self.database()
        self.tabel()
        self.insert()
        self.show()
        self.delete()