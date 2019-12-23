import csv

class yuki(object):
    def olahraga(self):
      with open('kelas_2c/yuki.csv', 'r') as kode:
          reader = csv.reader(kode, delimiter=',')
          for data in reader:
              print("Barang Tersedia", data)

