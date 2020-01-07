import sqlite3
import csv
import matplotlib.pyplot as plt
import requests

class Echa(object):
    
    
    def data(self):
        kode_barang="101"
        if(kode_barang[2]) =="1":
            print("Flashdisk")
        elif(kode_barang[2]) =="2":
            print("Mouse")

    def databarang(self):
        kode_barang="101"
        nama_barang="flashdisk"
        jumlah_awal="20"
        stok_akhir ="10"
        harga ="60000"
        with open('echa.csv') as data:
            csv_reader = csv.reader(data)
            for row in csv_reader:
                if str(row[0])==kode_barang:
                    if str(row[1]) ==nama_barang:
                        if str(row[2]) ==jumlah_awal:
                            if str(row[3]) ==stok_akhir:
                                if str(row[4]) ==harga:
                                    if len(str(row[1]))%2 == 0:
                                        try:
                                            print("data", kode_barang)
                                            print("kode",row[0], "nama", row[1],"jumlah",row[2], "stok", row[3], "harganya", row[4])
                                        except Exception as e:
                                            print(e)
                                            print("lakukan pengecekan ulang")
                                        
    def gudang(self):
        gudang1 = "1"
        gudang2 = "2"

        if gudang1 == "1":
            print("ELEKTRONIK")
        elif gudang2 == "2":
            print("ALAT_TULIS")
        else:
            print("BUKU")

    def barang_masuk(self):
        kode_barang = "105"
        nama_barang = "keyboard"
        jumlah = "25"
        tgl_masuk = "28-12-2019"
        
        print(kode_barang,nama_barang, jumlah, tgl_masuk)

    def barang_keluar(self):
        kode_barang1= "103"
        kode_barang2 = "106"
        nama_barang1 = "Fan"
        nama_barang2 = "Buku"
        jumlah_keluar1 = "5"
        jumlah_keluar2 = "30"
        tgl_keluar = "29-12-2019"

        if kode_barang1[2] =="3":
            print(nama_barang1,jumlah_keluar1,tgl_keluar)
        elif kode_barang2[2] =="6":
            print(nama_barang2,jumlah_keluar2,tgl_keluar)

    def koneksidb(self):
        koneksi = sqlite3.connect('database')
        cursor = koneksi.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS  \
                    DATA_GUDANG(KODE_BARANG REAL, NAMA_BARANG TEXT, JUMLAH_AWAL REAL, STOK_AKHIR REAL, HARGA REAL)')
        tampil = "SELECT * FROM DATA_GUDANG"
        cursor.execute("INSERT INTO DATA_GUDANG VALUES('101','Flashdisk','20', '10', '60000')")
        koneksi.commit()
        try:
            cursor.execute(tampil)
            results = cursor.fetchall()
            for row in results:
                KODE_BARANG = row[0]
                NAMA_BARANG = row[1]
                JUMLAH_AWAL = row[2]
                STOK_AKHIR = row[3]
                HARGA      = row[4]
                print ("kode_barang %s, dengan nama_barang %s, dengan jumlah_awal %s,  dengan stok_akhir %s, harganya %s" % \
                (KODE_BARANG, NAMA_BARANG, JUMLAH_AWAL, STOK_AKHIR, HARGA))
        except:
            print ("DATA TIDAK TERSEDIA")


    def suplier(self):
        suplier1="123"
        suplier2="124"
        if suplier1 == "123":
            print("bandung")
        elif suplier2 == "124":
            print("padang")
        else:
            print("padangpanjang")

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
        self.gudang()
        self.barang_masuk()
        self.barang_keluar()
        self.koneksidb()
        self.suplier()
        self.grafikpemasukan()
        self.request()
    
