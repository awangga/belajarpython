import matplotlib.pyplot as plt
import requests
import sqlite3

class dianmarkuci() :
    def __init__(self, kode, hargatotal, kuota):
        self.kode = kode
        self.hargatotal = hargatotal
        self.kuota = kuota
 
    def rental(self):       
        if (self.kode[1]) == "1":
            print("Avanza", "Innova", "APV")
        elif self.kode[1] == "2":
            print("Xenia", "Yaris", "Jeep")
        elif self.kode[1] == "3":
            print("Mobilio", "Hiace")
        elif self.kode[1] == "4":
            print("Brio", "Camry")
        else:
            print("Mobil tidak tersedia")
            
    def gimana(self):        
        if (self.kode[0]) =="P":
            print("Mobil BerAC depan belakang")
        elif (self.kode[0]) =="Q":
            print("Mobil BerAC depan saja")
    
    def status(self):
        if (self.kode[2]) =="A":
            print("Mobil tersedia 2 per harinya")
        elif (self.kode[0]) =="B":
            print("Mobil tersedia 3 per harinya")
        elif (self.kode[0]) =="C":
            print("Mobil tersedia 4 per harinya")
        else:
            print("Mobil tersedia 5 per harinya")
    
    def potongan(self):    
        if self.hargatotal > 500000 :
            try:
                print("mendapat potongan harga 5%")
            except Exception :
                print(Exception)

    def lebih(self):       
        if self.kuota > 4 :
            print (" kuota sudah melebihi")
        if (self.kode[0]) =="P":
            print ("Wajib asuransi")
        else:
            print ("Tidak perlu asuransi")
        if (self.kode[0]) =="Q":
            print ("wajib mendapat izin beroperasi")
        else:
            print ("tidak wajib mendapat izin beroperasi")


    def Database(self):
        koneksi = sqlite3.connect('db')
        cursor = koneksi.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS \
                       DATA_RENTAL(KODE TEXT , RENTAL TEXT, HARGATOTAL REAL)')
        tampilin = "SELECT * FROM DATA_RENTAL"
        cursor.execute("INSERT INTO DATA_RENTAL VALUES('A1','Avanza',400000)")
        koneksi.commit()
        try:
            
                cursor.execute(tampilin)
                results = cursor.fetchall()
                for row in results:
                    KODE   = row[0]
                    RENTAL = row[1]
                    HARGATOTAL  = row[2]
                    print ("KODE %s, dengan RENTAL %s, dari HARGATOTAL %s" % \
                    (KODE, RENTAL, HARGATOTAL))
        except:
            print ("Mobil tidak tersedia")

    def grafik(self):
        plt.plot([1,2,3,4,5,6,7,8,9,10,11,12],[60, 55, 70, 80, 95, 90, 86, 77, 87, 55, 58, 95])
        plt.show()    

    def reque(self):
        req = requests.get('https://github.com/dianmarkuci')
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
            
    def Jalanin(self):
       self.rental()
       self.gimana()
       self.status()
       self.potongan()
       self.lebih()
       self.Database()
       self.grafik()
       self.reque()