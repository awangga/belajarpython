import csv

class Gany(object):
    def Color(self):
        with open('kelas_2c/gany.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            bulann = []
            warnaa = []
            for row in readCSV:
                warna = row[1]
                bulan = row[0]
                bulann.append(bulan)
                warnaa.append(warna)
            
            print(bulann)
            print(warnaa)
