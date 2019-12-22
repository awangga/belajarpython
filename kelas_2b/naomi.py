import csv
class daftar(object):
    
    def siswa(self):
        with open('bio.csv', 'r') as filecsv:
            datafile = csv.reader(filecsv)
            for data in datafile:
                print(data)