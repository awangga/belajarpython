# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 19:08:20 2019

@author: Asus
"""


import sqlite3
import csv
import matplotlib.pyplot as plt
import requests


class helmi:
    def salam(self):
        print ("Selamat datang di Showroom kami")
        
    def stok(self):
        tes = open('kelas_2c/stok.csv')
        data = csv.reader(tes, delimiter= 'r')
        for row in data:
            print (row)
            
    def matp(self):
        plt.plot([4,8,13,17,20],[54, 67, 98, 78, 45])
        plt.show()
        
    
    def requ(self):
        req = requests.get('http://www.instagram.com/')
        req.encoding      # returns 'utf-8'
        req.status_code   # returns 200
        req.elapsed       # returns datetime.timedelta(0, 1, 666890)
        req.url           # returns 'https://www.instagram.com/'
        req.history       # returns [<Response [301]>, <Response [301]>]
        req.headers['Content-Type']
    
            
    def membuatdatabase(self):
        sqlite3.connect('stok.db')
        print("Database Berhasil Dibuat")
        
    def membuattabel(self):
        db = sqlite3.connect('stok.db')
        cursor = db.cursor()
        sql = """CREATE TABLE data (
        jenis VARCHAER(30),
        merk VARCHAR(30),
        tahun Varchar(30)
        )"""
        cursor.execute(sql)
        print("Tabel stok berhasil dibuat!")
        
        
        
    def insert(self):
        # Membuka  koneksi ke database
        db = sqlite3.connect('stok.db' )
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
        db = sqlite3.connect('stok.db')
        cursor = db.cursor()
        sql = "SELECT * FROM data"
        cursor.execute(sql)
        results = cursor.fetchall()
        for data in results:
            print(data)
            
            
    def hapus(self):
        db = sqlite3.connect('stok.db')
        cursor = db.cursor()
        cursor.execute('DELETE FROM data WHERE tahun=2006')
        db.commit()
        print("{} data dihapus".format(cursor.rowcount))
    
    def bareng(self):
        self.salam()
        self.stok()
        self.insert()
        self.show()
   
    
    