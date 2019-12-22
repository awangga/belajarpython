import csv

class rayhan:
    
    def plane (self):
        with open('kelas_2b/pesawat.csv') as rayhan:
            rey = csv.reader(rayhan, delimiter=',')
            for r in rey:
                if int(r[0]) > 19:
                    print ("Kamu Boleh beli Anggur")
                else:
                    print ("kamu Tidak Boleh Beli")  