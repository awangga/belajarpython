import csv
import requests 
import matplotlib.pyplot as plt
import sqlite3

class Puja:
    def __init__(self, rp):
        self.rp = rp

    def SitiNPK(self):
        with open('kelas_2b/pemrograman2.csv') as coba:
            csv_reader = csv.reader(coba, delimiter= ',')
            line= 0
            for baris in csv_reader:
                if line == 0:
                    print(f'{"=".join(baris)}')
                line += 0
                print(f'Processed {line} lines.')

    def kopos(self):
        kodepos = "35362"
        with open('kelas_2b/pemrograman2.csv') as coba:
            csv_reader = csv.reader(coba, delimiter= ',')
            for baris in csv_reader:
                if str(baris[3]) == kodepos:
                    print("di Bandara" , baris[0] , "Kode Pos" , baris[3])

    def harga(self):
        harga1 = 300000
        harga2 = 1000000
        harga3 = 800000
        hargaTotal1 = self.rp*harga1
        hargaTotal2 = self.rp*harga2
        hargaTotal3 = self.rp*harga3
        print("Tujuan TGK-CGK Pembayaran" , self.rp , "Tiket:",hargaTotal1) 
        print("Tujuan DJJ-CGK Pembayaran" , self.rp , "Tiket:",hargaTotal2)
        print("Tujuan BKS-CKG Pembayaran" , self.rp , "Tiket:",hargaTotal3) 

    def keterlambatan(self):
        print("Jika Keterlambatan")
        telat = [3,6,12]
        for i in telat:
            print("Jika keterlambatan",(i), "jam akan diberikan ganti rugi")

    def rute(self):
        bandara = "CGK"

        if bandara == "CGK":
            print("Bandara Internasional")
        elif bandara:
            print("Bandara Domestik")
        else:
            print("Bandara Domestik")

    def sq(self):
        koneksi = sqlite3.connect('bismillah.db')
        cursor = koneksi.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS \
                        JADWAL(HARI TEXT, MASKAPAI TEXT ,PENUMPANG TEXT)')
        tampil = "SELECT * FROM JADWAL" 
        cursor.execute("INSERT INTO JADWAL VALUES ('MINGGU','GARUDA','144')")
        koneksi.commit()
        try:
            cursor.execute(tampil)
            results = cursor.fetchall()
            for row in results:
                HARI            = row[0]
                MASKAPAI        = row[1]
                PENUMPANG       = row[2]
                print ("HARI %s,MASKAPAI %s,PENUMPANG %s" % \
                    (HARI, MASKAPAI, PENUMPANG))
        except:
            print("YHA JADWALNYA TIDAK TERSEDIA YHA")

    def grafik(self):
        plt.plot([1,2,3],[80,75,90])
        plt.show()

    def berangkat(self):
        ruteInternasional = 0
        while ruteInternasional < 15:
            print("Bandara Internasional")
            ruteInternasional = ruteInternasional + 1
        
    
    print("Bandara Domestik")

    def penghasilan(self):
        gaji= 100000000
        captain = True 

        if gaji > 50000000:
            print("Menduduki Jabatan Sebagai Captain Pilot")
            if captain:
                print("Jabatan Tertinggi didalam Pesawat")
            else: 
                print("Bukan Jabatan Tertinggi")
        else:
            print("Bukan Captain")

    def requests(self):
        req = requests.get('https://open.spotify.com/user/21ucxzotkiajpicbhms2ttteq/playlist/399VxZVeadUF0VjqJm8C2i?si=kQcVMWoLTKSue8MbsgCTrA')
        req.encoding      
        req.status_code   
        req.url           
        req.headers['Content-Type']
        try:
            print(req.status_code)
            print(req.encoding)
            print(req.headers)
            print(req.url)
        except Exception as e:
            print(e)

    def start(self):
        print("Bandara Domestik")
        self.SitiNPK()
        self.kopos()
        self.harga()
        self.keterlambatan()
        self.rute()
        self.grafik()
        self.berangkat()
        self.penghasilan()
        self.requests()