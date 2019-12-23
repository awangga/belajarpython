import csv

class nurul:

    def ganjilgenap(self):
        with open('kelas_2c/nurul.csv') as files:
            reader=csv.reader(files,  delimiter=',')
            for row in reader:
                if int(row[0])%2 == 1:
                    print(row[0],"merupakan Bilangan Ganjil")
                else:
                    print(row[0],"merupakan Bilangan Genap atau Bukan Bilangan Ganjil")
                
                    