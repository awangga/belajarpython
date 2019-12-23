import csv

class nurul(object):
    def __init__(self, hari):
        self.hari = hari


    def NurulKamila(self):
        with open('kelas_2c/nurul.csv','r') as ruangan:
            reader = csv.reader(ruangan)
            for row in reader:
                if str(row[0]) == self.hari:
                    print("pada hari", row[0], "tanggal", row[1], row[2], " meminjam ruangan", row[3])
                