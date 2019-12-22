import csv

class AkilMunawwar(object):
    
    def rekursi(self):
        with open("./kelas_2b/akil.csv") as abc:
            hooh = csv.reader(abc)
            for i in hooh:
                if i[0] == '1':
                    print('1')
                else:
                    print('gatau')