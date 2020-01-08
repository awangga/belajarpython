import csv
import sqlite3
import matplotlib.pyplot as plt
import requests

class hanifah() :
    def __init__(self, kode, penurunan, hargatotal, umur):
        self.kode = kode
        self.penurunan = penurunan
        self.hargatotal = hargatotal
        self.umur = umur
        
    def travel(self):
        if (self.kode[2]) == "1":
            print("Xtrans", "F-Trans", "Harum P")
        elif self.kode[2] == "2":
            print("Cititran", "Baraya", "Teletrans")
        elif self.kode[2] == "3":
            print("Daytrans", "Transline")
        elif self.kode[2] == "4":
            print("Cipaganti", "Primajasa")
        else:
            print("Travel tidak tersedia")  
            
    def clas(self):      
        if (self.kode[4]) =="M":
            print("Travel Bisnis(Dikasih Snack)")
        elif (self.kode[4]) =="N":
            print("Travel Ekonomi(Tidak dikasih snack)")
    
    def ketersediaan(self):
        if (self.kode[0]) =="A":
            print("Travel tersedia 3 travel per harinya")
        elif (self.kode[0]) =="B":
            print("Travel tersedia 5 travel per harinya")
        elif (self.kode[0]) =="C":
            print("Travel tersedia 8 travel per harinya")
        else:
            print("Travel tersedia 10 travel per harinya")
            
    def diskon(self):
        if self.hargatotal > 250000 :
            try:
                print("mendapat potongan harga 10%")
            except Exception :
                print(Exception)
                
    def penurunann(self):
            with open('kelas_2b/hanifah.csv') as files:
                reader=csv.reader(files,  delimiter=',')
                for row in reader:
                    if (self.kode[2]) == "1":
                        print("Xtrans", "F-Trans", "Harum P")
                    elif self.kode[2] == "2":
                        print("Cititran", "Baraya", "Teletrans")
                    elif self.kode[2] == "3":
                        print("Daytrans", "Transline")
                    elif self.kode[2] == "4":
                        print("Cipaganti", "Primajasa")
                    else:
                        print("Travel tidak tersedia") 
                        
    def supir(self):
        if self.umur > 25 :
            print (" umur sudah melebihi")
            if (self.kode[4]) =="M":
                print ("Wajib ikutan asuransi")
            else:
                print ("Tidak perlu ikutan asuransi")

            if (self.kode[4]) =="N":
                print ("wajib mendapatkan izin mengemudi")
            else:
                print ("tidak wajib mendapatkan izin mengemudi")
        else:
            print ("umur belum melebihi")

    def Database(self):                        
        koneksi = sqlite3.connect('db')
        cursor = koneksi.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS \
                    DATA_TRAVEL(KODE TEXT , TRAVEL TEXT, HARGA REAL, PENURUNAN TEXT)')
        tampil = "SELECT * FROM DATA_TRAVEL"
        cursor.execute("INSERT INTO DATA_TRAVEL VALUES('A-1-M','X-Trans',105000, 'Jakarta Barat')")
        koneksi.commit()
        try:
                cursor.execute(tampil)
                results = cursor.fetchall()
                for row in results:
                    KODE   = row[0]
                    TRAVEL = row[1]
                    HARGA  = row[2]
                    PENURUNAN  = row[3]
                    print ("KODE %s, dengan TRAVEL %s, dari HARGA %s, PENURUNAN %s" % \
                    (KODE, TRAVEL, HARGA, PENURUNAN))
        except:
                print ("Travel tidak tersedia")
        
    def grafikpenjual(self):
        plt.plot([1,2,3,4,5,6,7,8,9,10,11,12],[60, 55, 70, 80, 95, 90, 86, 77, 87, 55, 58, 95])
        plt.show()
        
    def reque(self):
        req = requests.get('https://www.traveloka.com/en/')
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
    def Program(self):
       self.travel()
       self.clas()
       self.ketersediaan()
       self.diskon()
       self.penurunann()
       self.supir()
       self.Database()
       self.grafikpenjual()
       self.reque()
       
       
       



    

               
                
                
               