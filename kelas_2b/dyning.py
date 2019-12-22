import csv

class Dyning():
    def __init__(self, hari):
        self.hari = hari

    def DyningAidaBatrishya(self):
        with open('kelas_2b/dyning.csv', 'r') as jadwal:
            reader = csv.reader(jadwal)
            for row in reader:
                if str(row[0]) ==  self.hari:
                    print("pada hari",row[0], "di kelas", row[1], "ada matkul", row[2],"pada jam", row[3])
                else:
                    "Data jadwal tidak ditemukan"
                