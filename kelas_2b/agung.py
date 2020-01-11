# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 17:33:13 2019

@author: Ahmad Agung Tawakkal
"""

import csv
import sqlite3
from matplotlib import pyplot as plt
import requests

class Tawa(object):
    def Color(self):
        with open('./kelas_2b/agung.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            bulann = []
            warnaa = []
            for row in readCSV:
                warna = row[1]
                bulan = row[0]
                bulann.append(bulan)
                warnaa.append(warna)
            
            print(bulann)
            print(warnaa)


#csv 
    #read file
    def csv1(self):
        with open('./kelas_2b/agung.txt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'{", ".join(row)}')
                    line_count += 1
                else:
                    print(f'\t{row[0]} bekerja di {row[1]} departemen, dan lahir dibulan {row[2]}.')
                    line_count += 1
            print(f'Processed {line_count} lines.')
    #read file
    def csv2(self):
        with open('./kelas_2b/agung1.txt') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            bulann = []
            warnaa = []
            for row in readCSV:
                warna = row[1]
                bulan = row[0]
                bulann.append(bulan)
                warnaa.append(warna)
            
            print(bulann)
            print(warnaa)
    #create file        
    def csv3(self):
        with open('./kelas_2b/AgungBuat.txt', mode='w') as buat_file:
            mahasiswa_writer = csv.writer(buat_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
            mahasiswa_writer.writerow(['NPM', 'NAMA', 'JURUSAN','KELAS'])
            mahasiswa_writer.writerow(['1184015','Ahmad', 'IT', 'D4 2B'])
            mahasiswa_writer.writerow(['1184115','Agung', 'IT', 'D4 2B'])
            mahasiswa_writer.writerow(['1184005','Tawakkal', 'IT', 'D4 2B'])
    
#databse
    #buat database
    def database1(self):
        try:
            sqliteConnection = sqlite3.connect('./kelas_2b/mantap.db')
            cursor = sqliteConnection.cursor()
            print("Membuat Database")
        
            sqlite_select_Query = "select sqlite_version();"
            cursor.execute(sqlite_select_Query)
            record = cursor.fetchall()
            print("SQLite Database Version: ", record)
            cursor.close()
        
        except sqlite3.Error as error:
            print("Koneksi ke sqlite error!", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                
    #buat table
    def database2(self):
        try:
            sqliteConnection = sqlite3.connect('./kelas_2b/mantap.db')
            membuat_tabel = '''CREATE TABLE t_mahasiswa (
                                        npm INTEGER PRIMARY KEY,
                                        nama TEXT NOT NULL,
                                        email VARCHAR2 NOT NULL UNIQUE
                                        );'''
        
            cursor = sqliteConnection.cursor()
            print("Koneksi ke sqlite berhasil")
            cursor.execute(membuat_tabel)
            sqliteConnection.commit()
            print("Membuat Table")
        
            cursor.close()
    
        except sqlite3.Error as error:
            print("Error membuat table!", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                
    #input
    def database3(self):
        try:
            sqliteConnection = sqlite3.connect('./kelas_2b/mantap.db')
            mericord_tabel  = '''INSERT INTO t_mahasiswa (
                                        npm,
                                        nama,
                                        email
                                        ) VALUES (
                                        1,
                                        'Ahmad Agung Tawakkal',
                                        'Mantap@gmail.com'
                                        );'''
        
            cursor = sqliteConnection.cursor()
            print("Koneksi ke sqlite berhasil")
            cursor.execute(mericord_tabel)
            sqliteConnection.commit()
            print("Data berhasil di ricod")
            cursor.close()
    
        except sqlite3.Error as error:
            print("Error ricord data!", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                
    #tampil data
    def database4(self):
        try:
            sqliteConnection = sqlite3.connect('./kelas_2b/mantap.db')
            menampilkan_ricord = '''SELECT * FROM t_mahasiswa'''
            
            cursor = sqliteConnection.cursor()
            print("Koneksi ke sqlite berhasil")
            cursor.execute(menampilkan_ricord)
            sqliteConnection.commit()
            records = cursor.fetchall()
            print("Menampilkan Ricord Tabel Mahasiswa")
            for row in records:
                print ("npm",row[0])
                print ("nama",row[1])
                print ("email",row[2])
                print("\n")
            cursor.close()
            
        except sqlite3.Error as error:
            print("Error menampilkan data!", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()

    
#matplotlib 
    def matplotlib1(self):
        #produk makan yang di hasilkan pada perusahaan selama 5 bulan
        #bulan = [1,2,3,4,5]
        
        p1 =[7,8,6,11,7]
        p2 = [2,3,4,3,2]
        p3 =[7,8,7,2,3]
        p4 = [8,5,7,8,13]
        p5 = [10,3,5,3,14]
        hasil = [7,2,4,13,7]
        nama_perusahaan = ['Toko Snack','PT Cempaka','PT Prima Sinar Mulia','PT Sky Food Indutry','PT Rasa Mutu Utama']
        cols = ['c','m','r','b','y']
         
        plt.pie(hasil,
          labels=nama_perusahaan,
          colors=cols,
          startangle=90,
          shadow= True,
          explode=(0,0.05,0,0.05,0),
          autopct='%1.1f%%')
         
        plt.title('Diagram Hasil Produk Makanan Yang Dihasilkan Oleh Perusahaan Selama 5 Bulan')
        plt.show()
        #mencari titik
    def matplotlib2(self):
        x = [2,4,6,10,11,15]
        y = [6,8,5,10,9,11]
        plt.plot(x,y)
        plt.title('Mencari Titik')
        plt.ylabel('Sumbu Y')
        plt.xlabel('Sumbu X')
        plt.show()    
    
#request
    def request1(self):
        x = requests.get('https://www.youtube.com/watch?v=vD7qtYhTLEQ')

        print(x.text)
        #contoh jika link benar
    def request2(self):
        x = requests.get('https://github.com/')
        print(x.status_code)
        if x:
            print('Respon Mantap')
        else:
            print('Respon Tak Mantap')
        #contoh jika link salah
    def request3(self):
        x = requests.get('https://github.com/asdas asd123 3213')
        print(x.status_code)
        if x:
            print('Respon Mantap')
        else:
            print('Respon Tak Mantap')
    
    def Mantap(self):
        self.Color()
        self.csv1()
        self.csv2()
        self.csv3()
        self.database1()
        self.database2()
        self.database3()
        self.database4()
        self.matplotlib1()
        self.matplotlib2()
        self.request1()
        self.request2()
        self.request3()