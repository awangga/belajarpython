import csv

class Dyning(object):
    def __init__(self, hari, kelas):
        self.hari = hari
        self.kelas = kelas

    def DyningAidaBatrishya(self):
        with open('kelas_2b/dyning.csv', 'r') as jadwal:
            reader = csv.reader(jadwal)
            for row in reader:
                if str(row[0]) ==  self.hari:
                    if str(row[1]) == self.kelas:
                        if len(str(row[1]))%2 == 0:
                            try:
                                print("jadwal", self.kelas)
                                print("pada hari",row[0], "di kelas", row[1], "ada matkul", row[2],"pada jam", row[3])
                            except Exception as e:
                                print(e)
                                print("coba cek penulisan kelas kembali")