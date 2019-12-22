import csv

class hanifah:

    def ganjilgenap(self):
        with open('./kelas_2b/hanifah.csv') as files:
            reader=csv.reader(files,  delimiter=',')
            for row in reader:
                if int(row[0])%2 == 1:
                    print(row[0],"adalah bilangan ganjil")
                else:
                    print(row[0],"adalah bilangan genap")
                
                    

                
                
               