import csv

class Puja:
    def SitiNPK(self):
        with open('kelas_2b/pemrograman.csv') as coba:
            csv_reader = csv.reader(coba, delimiter= ',')
            line= 0
            for baris in csv_reader:
                if line == 0:
                    print(f'{"=".join(baris)}')
                line += 0
                print(f'Processed {line} lines.')