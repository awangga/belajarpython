import csv

class alvian:
    
    def uang(self):
        with open('kelas_2c/alvian.csv') as file:
            datanya = csv.reader(file, delimiter=',')
            for r in datanya:
                if int(r[0]) == 20000:
                    print ("aku lumayan kaya loh")
                elif int(r[0]) == 30000:
                    print ("Disini Kaya boy")
                elif int(r[0]) == 21000:
                    print ("masih miskin loh :(")
                else:
                    print ("kurang kaya aku")
