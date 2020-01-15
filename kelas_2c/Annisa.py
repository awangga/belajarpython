# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 17:21:10 2019

@author: NISA
"""
import sqlite3
import csv
import requests
import matplotlib.pyplot as plt

class Annisa_Khairani():
    def __init__(self, motor):
        self.motor = motor
        
    def Annisa(self):
        with open ('kelas_2c/AnnisaK.csv', 'r') as penjualan:
            reader = csv.reader(penjualan)
            for row in reader:
                    print(row)
           
    def data(self):
        motor="101"
        if(motor[2]) =="1":
            print("N-Max")
        elif(motor[0]) =="2":
            print("Yamaha Mio")

    def databarang(self):
        motor="a"
        warna="Hitam"
        nama="N-Max"
        harga ="17700000"
        with open('kelas_2c/AnnisaK.csv') as data:
            csv_reader = csv.reader(data)
            for row in csv_reader:
                if str(row[0])==motor:
                    if str(row[1]) ==warna:
                        if str(row[2]) ==nama:
                            if str(row[3]) ==harga:
                                    if len(str(row[1]))%2 == 0:
                                        try:
                                            print("data", motor)
                                            print("motor",row[0], "warna", row[1],"nama",row[2], "harganya", row[3])
                                        except Exception as e:
                                            print(e)
                                            print("lakukan pengecekan ulang")
                                        
    def peralatan(self):
        peralatan1 = "1"
        peralatan2 = "2"

        if peralatan1 == "1":
            print("Kaca_Spion")
        elif peralatan2 == "2":
            print("Helm")
        else:
            print("Helm_Ink")

    def motor_masuk(self):
        motor = "d" 
        warna = "Hitam"
        nama = "Vario"
        jumlah = "20"
        tgl_masuk = "26-12-2019"
        
        print(motor,warna,nama,jumlah, tgl_masuk)

    def motor_keluar(self):
        motor1= "103"
        motor2 = "e"
        nama1 = "Beatpop"
        nama2 = "SupraX"
        jumlah_keluar1 = "10"
        jumlah_keluar2 = "15"
        tgl_keluar = "27-12-2019"

        if motor1[2] =="3":
            print(nama1,jumlah_keluar1,tgl_keluar)
        elif motor2[2] =="3":
            print(nama2,jumlah_keluar2,tgl_keluar)

    def koneksidb(self):
        koneksi = sqlite3.connect('database')
        cursor = koneksi.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS  \
                    DATA_GUDANG(motor REAL, warna TEXT, nama REAL, harga REAL)')
        tampil = "SELECT * FROM DATA_GUDANG"
        cursor.execute("INSERT INTO DATA_GUDANG VALUES('a','Hitam','N-Max', '17700000')")
        koneksi.commit()
        try:
            cursor.execute(tampil)
            results = cursor.fetchall()
            for row in results:
                motor = row[0]
                warna = row[1]
                nama = row[2]
                harga= row[3]
                print ("motor%s, dengan warna %s, dengan nama %s,  dengan harganya %s" % \
                (motor, warna, nama, harga))
        except:
            print ("DATA TIDAK TERSEDIA")


    def suplier(self):
        suplier1="133"
        suplier2="134"
        if suplier1 == "133":
            print("bogor")
        elif suplier2 == "134":
            print("Jakarta")
        else:
            print("Jakartaselatan")

    def grafikpemasukan(self):
        plt.plot([1,2,3,4,5,6,7,8],[87, 90, 95, 93, 85, 86, 90, 97])
        plt.show()
    def request(self):
        req = requests.get('https://www.wattpad.com/')
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

    def panggil(self):
        self.data()
        self.databarang()
        self.peralatan()
        self.motor_masuk()
        self.motor_keluar()
        self.koneksidb()
        self.suplier()
        self.grafikpemasukan()
        self.request()
           