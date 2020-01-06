# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 17:33:13 2019

@author: Ahmad Agung Tawakkal
"""

import csv
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
        self.matplotlib1()
        self.matplotlib2()
        self.request1()
        self.request2()
        self.request3()