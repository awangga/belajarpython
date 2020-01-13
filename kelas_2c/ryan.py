import sqlite3
import csv
import matplotlib.pyplot as plt
import requests
class ryan:
    def awal(self):
        print ("Welcome to jungle")
        
    def gudang(self):
        tes = open('kelas_2c/ryan.csv')
        data = csv.reader(tes, delimiter= 'r')
        for row in data:
            print (row)
            
    def matplotlib(self):
        plt.plot([4,8,13,17,20],[54, 67, 98, 78, 45])
        plt.show()
        
    
    def reqq(self):
        req = requests.get('https://github.com/awangga/belajarpython/')
        req.encoding
        req.status_code
        req.elapsed
        req.url           
        req.history
        req.headers['Content-Type']
    
            
    def createdatabase(self):
        sqlite3.connect('ryan.db')
        print("Database Berhasil Dibuat")
        
    def createtabel(self):
        db = sqlite3.connect('ryan.db')
        cursor = db.cursor()
        sql = """CREATE TABLE data (
        jenis VARCHAER(30),
        merk VARCHAR(30),
        tahun Varchar(30)
        )"""
        cursor.execute(sql)
        print("Udah buat ya!")
        
        
        
    def insert(self):
        # Membuka  koneksi ke database
        db = sqlite3.connect('ryan.db' )
        # menyiapkan method menggunakan db cursor
        cursor = db.cursor()
        # kodingan untuk insert
        sql = """INSERT INTO data(jenis, merk, tahun)
        VALUES ('sedan', 'starlet', '2006')"""
            # Execute  SQL command
        cursor.execute(sql)
            # masuk datanya ke database
        db.commit()
        print("{} data berhasil ditambahkan".format(cursor.rowcount))
    

        
    def show(self):
        db = sqlite3.connect('ryan.db')
        cursor = db.cursor()
        sql = "SELECT * FROM data"
        cursor.execute(sql)
        results = cursor.fetchall()
        for data in results:
            print(data)
            
            
    def hapus(self):
        db = sqlite3.connect('ryan.db')
        cursor = db.cursor()
        cursor.execute('DELETE FROM data WHERE tahun=2006')
        db.commit()
        print("{} data dihapus".format(cursor.rowcount))
    
    def runing(self):
        self.awal()
        self.gudang()
        self.insert()
        self.show()