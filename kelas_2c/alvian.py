import csv
import matplotlib.pyplot as plt
import numpy as np 
import time
import os
import sqlite3
import requests

class alvian:
    #Buat Manggil semua aja .
    def MataBatin(self):
        self.nomor()
        self.nama()
        self.uang()
        self.Matplotlib()
        self.cobaWhile()
        self.CobaTabel()
        self.InputData()
        self.ViewData()
        self.requestaja()
        self.requestaja2()
 
    #method if, if else, if elif else :
    def nomor(self):
        with open('kelas_2c/alvian.csv') as file:
            datanya = csv.reader(file, delimiter=',')
            for r in datanya:
                if int(r[0]) < 30000:
                    print ("Bayar",(r[1]))
                    
    def nama(self):
        with open('kelas_2c/alvian.csv') as file:
            datanya = csv.reader(file, delimiter=',')
            for r in datanya:
                if int(r[0]) == 20000:
                    print ((r[1]),"nama paling keren")
                else:
                    print ((r[1]),"bukan alvian Oy")

    def uang(self):
        with open('kelas_2c/alvian.csv') as file:
            datanya = csv.reader(file, delimiter=',')
            for r in datanya:
                if int(r[0]) == 20000:
                    print ("punya uang Rp.",(r[0]),"aku lumayan kaya loh","atas nama",(r[1]))
                elif int(r[0]) == 30000:
                    print ("punya uang Rp.",(r[0]),"Disini Kaya boy","atas nama",(r[1]))
                elif int(r[0]) == 21000:
                    print ("punya uang Rp.",(r[0]),"masih miskin loh :)","atas nama",(r[1]))
                else:
                    print ("punya uang Rp.",(r[0]),"kurang kaya aku","atas nama",(r[1]))

#Penggunaan Matplotlib  
    def Matplotlib(self):
        x = np.arange(0, 3 * np.pi, 0.1)
        y_sin = np.sin(x)
        y_cos = np.cos(x)
        plt.subplot(2, 1, 1)

        # buat awal plot
        plt.plot(x, y_sin)
        plt.title('Sine')
        plt.subplot(2, 1, 2)
        plt.plot(x, y_cos)
        plt.title('Cosine')
        plt.savefig("kelas_2c/vian_Matplotlib.png")

        # nampilin Gambar Matplotib
        plt.show()
 
  # Penggunaan While Aja Dulu 
    def cobaWhile(self):
        list1 = open('kelas_2c/alvian.txt','r') 
        list2 = list1  
        list1 = iter(list1) 
        print ("The contents of list are : ") 
         
        start_next = time.time() 
        while (1) : 
                val = next(list1,'end') 
                if val == 'end': 
                 break
        else : 
                print (val) 
                print ("Time taken for next() is : " + str(time.time() - start_next)) 
    
        start_for = time.time() 
        for i in list2 : 
                print (i) 
                print ("Time taken for loop is : " + str(time.time() - start_for)) 

#Database Proses Create, Input, View 
    def CobaTabel(self):
        try:
            self.connection = sqlite3.connect('./kelas_2c/alvianpunya.db')
            self.cursor = self.connection.cursor()

            self.cursor.execute('CREATE TABLE vian (id INTEGER PRIMARY KEY, nama VARCHAR(50), rupiah VARCHAR(50))')
        except:
            print("Failed Tabel Again Coyy!")

    def InputData(self):
        try:
            self.cursor.execute('INSERT INTO vian VALUES(?, ?, ?)', (1, "alvian", "Dua Puluh Ribu"))
            self.cursor.execute('INSERT INTO vian VALUES(?, ?, ?)', (2, "sinaga", "Tiga Puluh Ribu"))
            self.cursor.execute('INSERT INTO vian VALUES(?, ?, ?)', (3, "daniel", "Tiga Puluh lima Ribu"))
            self.connection.commit()
        except:
            print("Failed Table Again Coyy!")

    def ViewData(self):
        self.cursor.execute('SELECT * FROM vian')
        row = self.cursor.fetchone()

        nama = row[1]
        rupiah = row[2]

        print("nama : " + str(nama))
        print("rupiah : " + str(rupiah))

        self.connection.commit()

#Request File and Linkweb
    def requestaja(self):
        i = requests.get('https://www.youtube.com/watch?v=rJHCtij6vaA&list=RDrJHCtij6vaA&start_radio=1')

        print(i.text)

    def requestaja2(self):
        i = requests.get('https://github.com/cemewew asd123 3213')
        print(i.status_code)
        if i:
            print('Belajar Yang pinter aja dulu')
        else:
            print('banyak banyak Doa :)')