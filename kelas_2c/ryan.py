import csv
class hitung(object):
    
    def kali(self):
        with open('kelas_2c/pemrograman.csv')as csv_f:
            csv_r = csv.reader(csv_f, delimiter=',')
            for row in csv_r:
                print(f'\t{row[0]} * {row[1]} = {row[2]}.')