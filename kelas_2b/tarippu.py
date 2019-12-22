import csv

class Tari:
    def main(self):
        with open('./kelas_2b/tarippu.csv') as csv_files:
            reader=csv.reader(csv_files)
            for kartu in reader:
                if kartu[0] == '0':
                    print('tidak ada apa-apa')
                else:
                    print('ini',kartu[0], 'dengan tipe',kartu[1])