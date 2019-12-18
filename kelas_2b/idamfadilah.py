import csv
import random

class idamfadilah:
    def angka(self):
        with open('./kelas_2b/idamfadilah.csv') as files:
            reader=csv.reader(files)
            row_count = sum(1 for row in reader)
            angka=random.randint(1,row_count)
            return angka
    def giveaway(self,number):
        with open('./kelas_2b/idamfadilah.csv') as files:
            reader=csv.reader(files,  delimiter=',')
            for row in reader:
                if int(row[0]) == number:
                    print("Selamat kepada Sdr.",row[1],",anda berhak mendapatkan iphone X")


                
                
               