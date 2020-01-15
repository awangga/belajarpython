# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 17:32:34 2020

@author: ASUS
"""
import csv
import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import requests

class yuki:
        def item(self):
            with open('kelas_2c/yuki.csv') as kode:
                reader = csv.reader(kode)
                line_count = 0
                for row in reader:
                    if line_count == 0:
                        print(f'Column names are {", ".join(row)}')
                        line_count += 1
                    else:
                        print(f'\t Code Name {row[0]} Item {row[1]} , Price {row[2]}.')
                line_count += 1
                print(f'Processed {line_count} lines.')
                
        def data(self):
            with open('kelas_2c/yuki.csv', 'r') as kode:
                reader = csv.reader(kode, delimiter=',')
                for data in reader:
                    print("Barang Tersedia", data)
        
        def tambah_data_scv(self):
            with open('yuki.csv', mode='a') as kode:
                
                writer = csv.DictWriter(kode, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writeheader()
                writer.writerow({'KODE': 'A005', 'BARANG': 'MATRAS', 'HARGA': '21500'})
        print("Barang  Telah Tertambah!")
    
                    
        def mat1(self):
                        fig = plt.figure()
                        ax = fig.add_subplot(111)
                        ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
                        ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
                        ax.set_xlim(0.5, 4.5)
                        plt.show()
                        
        def mat2(self):
            
                ### 2 dimension
                c = np.array([(1,2,3),
                              (4,5,6)])
                print(c.shape)

                ### 3 dimension
                d = np.array([
                        [[1, 2,3],
                         [4, 5, 6]],
                         [[7, 8,9],
                          [10, 11, 12]]
                         ])
                print(d.shape)
        
        def create(self):
            sqlite3.connect('penjualan.db')
            print("Database telah Dibuat")
        
        def table(self):
            conn = sqlite3.connect('penjualan.db')
            print ("Opened database successfully")

            conn.execute('''CREATE TABLE PEMBELI
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         BARANG         TEXT     NOT NULL,
         HARGA          INT);''')
        print ("Table created successfully")
            
        
        
        
        
        def insert(self):
            conn = sqlite3.connect('penjualan.db')

            conn.execute("INSERT INTO PEMBELI VALUES(1,'YUKI','TOYA', 23000)")
            conn.execute("INSERT INTO PEMBELI VALUES(2,'ARDI','SAMSAK', 43000)")
            conn.execute("INSERT INTO PEMBELI VALUES(3,'ANSYAH','TARGET', 52000)")
            

            conn.commit()
            print ("Records created successfully")
            conn.close()
        
        def select(self):
            conn = sqlite3.connect('penjualan.db')
            print ("Opened database successfully")

            cursor = conn.execute("SELECT ID, NAME, BARANG, HARGA from PEMBELI")
            for row in cursor:
                print ("ID = ", row[0])
                print ("NAME = ", row[1])
                print ("BARANG = ", row[2])
                print ("HARGA = ", row[3], "\n")
   
            print ("Operation done successfully")
            conn.close()
        
        def delete(self):
            conn = sqlite3.connect('penjualan.db')
            print ("Opened database successfully");

            conn.execute("DELETE from PEMBELI where ID = 2;")
            conn.commit()
            print ("Total number of rows deleted :"), conn.total_changes

            cursor = conn.execute("SELECT ID, NAME, BARANG, HARGA from PEMBELI")
            for row in cursor:
                print ("ID = ", row[0])
                print ("NAME = ", row[1])
                print ("BARANG = ", row[2])
                print ("HARGA = ", row[3], "\n")

            print ("Operation done successfully")
            conn.close()
            
        def request(self):
            req = requests.get('https://github.com/awangga/belajarpython')
 
            req.encoding 
            req.status_code
            req.elapsed 
            req.url 
            req.history 
            req.headers['Content-Type']
            
        def jalankan(self):
            self.item()
            self.data()
            self.mat1()
            self.mat2()
            self.create()
            self.table()
            self.insert()
            self.select()
            self.delete()
            self.request()