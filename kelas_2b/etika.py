import csv

class EtikaKL:
    def Kumpulan(self):
        
        #tentukan lokasi file, nama file, dan inisialisasi csv
        self.f = open('kelas_2b/Etika.csv','r')
        self.reader = csv.reader(self.f)

        #membaca baris per baris
        for row in self.reader:
            print (row)

        #menutup file csv
        self.f.close()