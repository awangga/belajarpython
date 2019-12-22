import csv
class sharif():
    def rokok(self):
        with open('kelas_2b/uduts.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            next(csv_reader)

            for line in csv_reader:
                #print(line[1])

                if int(line[1]) > 22000:
                        print( line[0] + " " + "mahal")
                else:
                        print(line[0]+" "+ "murah")

