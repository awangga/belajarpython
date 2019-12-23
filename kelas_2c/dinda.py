import csv

class dinda(object):
    def __init__(self, bulan):
        self.bulan = bulan


    def DindaAnik(self):
        with open('kelas_2c/DINDAA.csv','r') as Biaya:
            reader = csv.reader(Biaya)
            for row in reader:
                if str(row[0]) == self.bulan:
                    print("hari", row[0], "Nama", row[1], "Keluhan", row[2], " Biaya", row[3])
                
                        