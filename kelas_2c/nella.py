# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 15:26:42 2020

@author: Asus
"""
import matplotlib.pyplot as plt
import csv
import requests
import sqlite3 as lite


class nella:
    def belajar(self):
        tes = open('kelas_2c/nella.csv')
        data = csv.reader(tes, delimiter= 'r')
        for row in data:
            print (row)
                
                
    def Nel (self):
        plt.plot([4,8,13,17,20],[54, 67, 98, 78, 45])
        plt.show()
    
    def requre(self):
        req = requests.get('https://www.pinterest.ca/')
        req.encoding      
        req.status_code   
        req.elapsed       
        req.url           
        req.history       
        req.headers['Content-Type']

           
    def buat(self):
    
        con = lite.connect('test.db')
        print("Anak berhasil dibuat")
        
        with con:
        
            cur = con.cursor()
        
            cur.execute("CREATE TABLE cars(id INT, name TEXT, price INT)")
            cur.execute("INSERT INTO cars VALUES(1,'Audi',52642)")
            cur.execute("INSERT INTO cars VALUES(2,'Mercedes',57127)")
            cur.execute("INSERT INTO cars VALUES(3,'Skoda',9000)")
            cur.execute("INSERT INTO cars VALUES(4,'Volvo',29000)")
            cur.execute("INSERT INTO cars VALUES(5,'Bentley',350000)")
            cur.execute("INSERT INTO cars VALUES(6,'Citroen',21000)")
            cur.execute("INSERT INTO cars VALUES(7,'Hummer',41400)")
            cur.execute("INSERT INTO cars VALUES(8,'Volkswagen',21600)")
            
    def tampil(self):
        con = lite.connect('test.db')

        with con:

            cur = con.cursor()
            cur.execute("SELECT * FROM cars")

            rows = cur.fetchall()

            for row in rows:
                print (row)
    def kosong(self):
        con = lite.connect('test.db')
        cursor = con.cursor()
        cursor.execute('DELETE FROM cars WHERE price=52642')
        con.commit()
        print("{} data dihapus".format(cursor.rowcount))
        
    def asyuu(self):
            print ("THANK YOU NEXT")   
            
    def pekalahh(self):
        kode_kodean="101"
        if(kode_kodean[2]) =="1":
            print("Pc")
        elif(kode_kodean[2]) =="2":
            print("Monitor")    
            
    def coming(self):
        kode_barang = "200"
        nama_barang = "geprek stimlog"
        jumlah = "10"
        tgl_masuk = "12-12-2020"  
        print(kode_barang,nama_barang, jumlah, tgl_masuk)  
     
    def telat(self):
        print("Jika Keterlambatan")
        telat = [4,7,22]
        for i in telat:
            print("Jika keterlambatan",(i), "jam akan diberikan ganti rugi")
    
    def test(self):
        self.belajar()
        self.Nel()
        self.requre()
        self.buat()
        self.tampil()
        self.kosong()
        self.asyuu()
        self.pekalahh()
        self.coming()
        self.telat()