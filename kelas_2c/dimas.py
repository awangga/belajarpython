import csv
class maulana:
    def ojek(self):
            with open('kelas_2c/ojek.csv', 'r') as csvfile:
                readCSV = csv.reader(csvfile)
                harga = []
                tujuan = []
                for row in readCSV:
                    tujuansaya = row[0]
                    hargaojek = row[1]
                    print(row[0], row[1])

            harga.append(hargaojek)
            tujuan.append(tujuansaya)