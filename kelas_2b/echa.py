import csv

class echa:
    def werehousing(self):
        with open('kelas_2b/echa.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            for row in csv_reader:
                    print("menampilkan data barang:", row[0], row[1], row[2], row[3], row[4])
