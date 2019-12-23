import csv
import random




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
