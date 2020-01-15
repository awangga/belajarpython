import csv
import random
import matplotlib.pyplot as plt
import requests


class rizalramadhan (object):
    
    
    
               
    def pesan(self):
        with open('./kelas_2c/rizalramadhan.csv') as files:
            reader=csv.reader(files)
            row_count = sum(1 for row in reader)
            pesan=random.randint(1,row_count)
            return pesan
        
    def menu(self,pilih):
        with open('./kelas_2c/rizalramadhan.csv') as files:
            reader=csv.reader(files,  delimiter=',')
            for row in reader:
                if int(row[0]) == pilih:
                    print("pesanan anda adalah",row[1],"lokasi",row[2])

    def halo(self):
        print ("Selamat datang di gofood kami")
    
        
    def matp(self):
        plt.plot([8,10,13,17,20],[54, 67, 70, 78, 45])
        plt.show()
        
    def lihatmakanan(self):
      with open('./kelas_2c/rizalramadhan.csv', 'r') as kode:
          reader = csv.reader(kode, delimiter=',')
          for data in reader:
                 print("makanan Tersedia", data)

    def link(self):
        x = requests.get('https://w3schools.com/python/demopage.htm')

        print(x.text)   
        
    def makanan(self):
      with open('./kelas_2c/rizalramadhan.csv', 'r') as file:
          sic = csv.reader(file, delimiter=',')
          for row in sic:
              print("nomor",row[0], "nama", row[1], "lokasi", row[2])
        
    def run(self):
             self.halo()
             self.matp()
             self.lihatmakanan()
             self.link()
             self.makanan()
      