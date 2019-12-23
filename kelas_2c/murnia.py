import csv

class Mur:
    def mur(self,npm):
        print("Masukan NPM:")
        if len(npm)<6:
            print("npm kurang dari 6 digit")
        elif len (npm)>7:
            print("npm lebih dari 6 digit")
        else:
            with open('kelas_2c/mur.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    if row[0] == npm:
                        print(row[0], row[1], row[2])
                    else:
                        print("Tidak Ada Data")        