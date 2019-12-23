import csv

class alvian:
    #method if, if else, if elif else :
    def nomor(self):
        with open('kelas_2c/alvian.csv') as file:
            datanya = csv.reader(file, delimiter=',')
            for r in datanya:
                if int(r[0]) < 30000:
                    print ("Bayar",(r[1]))
                    
    def nama(self):
        with open('kelas_2c/alvian.csv') as file:
            datanya = csv.reader(file, delimiter=',')
            for r in datanya:
                if int(r[0]) == 20000:
                    print ((r[1]),"nama paling keren")
                else:
                    print ((r[1]),"bukan alvian Oy")

    def uang(self):
        with open('kelas_2c/alvian.csv') as file:
            datanya = csv.reader(file, delimiter=',')
            for r in datanya:
                if int(r[0]) == 20000:
                    print ("punya uang Rp.",(r[0]),"aku lumayan kaya loh","atas nama",(r[1]))
                elif int(r[0]) == 30000:
                    print ("punya uang Rp.",(r[0]),"Disini Kaya boy","atas nama",(r[1]))
                elif int(r[0]) == 21000:
                    print ("punya uang Rp.",(r[0]),"masih miskin loh :)","atas nama",(r[1]))
                else:
                    print ("punya uang Rp.",(r[0]),"kurang kaya aku","atas nama",(r[1]))
