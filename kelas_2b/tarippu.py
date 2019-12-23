import csv

class Tari():
    def main(self):
        with open('./kelas_2b/tarippu.csv') as csv_files:
            reader=csv.reader(csv_files)
            for kartu in reader:
                print (str(kartu[0][-3:]))