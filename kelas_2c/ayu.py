import sqlite3
import csv
import matplotlib.pyplot as plt
import requests

class Ayu(object):
  
   def tujuan(self):
        baris1 = "BDG"
        baris2 = "JKT"
        baris3 = "LPG"
        try:
            if baris1 == "BDG":
                print("Bandung")
            elif baris2 == "JKT":
                print("Jakarta")
            elif baris3 == "LPG":
                print("Lampung")
            else:
                print("Tujuan lainnya")
        except Exception as a:
            print(a)
            print("cek ulang")
            
   def customer(self):
            print("cek kembali data anda") 
            
   def tiket(self):
        no_customer = "123"
        no_tiket = "110"
        jumlah_tiket = "2"
        tgl_berangkat = "28-12-2019"
        print(no_customer, no_tiket, jumlah_tiket, tgl_berangkat)
        
   def csv(self):       
     #lokasi file dan nama csv yang telah disimpan
         with open('kelas_2c/ayu.csv') as csvfile:
    #untuk membaca dan  menampilkan semua data yang ada di file
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                print(row)
    
    
   def koneksidb(self):
        koneksi = sqlite3.connect('database')
        cursor = koneksi.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS  \
                    DATA_PENUMPANG(NO_IDENTITAS, NAMA_PENUMPANG, ALAMAT_PENUMPANG, NO_HP)')
        tampil = "SELECT * FROM DATA_PENUMPANG"
        cursor.execute("INSERT INTO DATA_PENUMPANG VALUES('123','BUDI','SARIASIH','087898675432')")
        koneksi.commit()
        try:
            cursor.execute(tampil)
            results = cursor.fetchall()
            for row in results:
                NO_IDENTITAS        = row[0]
                NAMA_PENUMPANG      = row[1]
                ALAMAT_PENUMPANG    = row[2]
                NO_HP               = row[3]
               
                print ("no_identitas %s, dengan nama_penumpang %s, dengan alamat_penumpang %s,  dengan no_hp %s" % \
                (NO_IDENTITAS, NAMA_PENUMPANG, ALAMAT_PENUMPANG, NO_HP))
        except:
            print ("DATA TIDAK ADA")


   def grafikpenumpang(self):
        print("Berikut adalah grafik perkembangan penumpang setiap bulan, harap bersabar")
        try:
            plt.plot([1,2,3,4,5,6],[1200, 1000, 1500, 2000, 900, 5000])
            plt.xlabel('Bulan')
            plt.ylabel('Penumpang')
            plt.title('Grafik Perkembangan rata-rata penumpang setiap bulan')
            plt.show()
        except Exception as e:
            print(e)
            
   def request(self):
        req = requests.get('https://www.zigzagbatam.com/category/tas')
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
            
   def request2(self):
        y = requests.get('https://rumus.co.id/contoh-cv-bahasa-inggris/')

        print(y.text)       
            
    
   def panggila(self):
        self.tujuan()
        self.customer()
        self.tiket()
        self.csv()
        self.koneksidb()
        self.grafikpenumpang()
        self.request()
        self.request2()
          
            