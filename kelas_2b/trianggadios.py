import csv



class TriAngga(object):
    def __init__(self, keyword):
        self.keyword = keyword

    def run(self):
        self.loadcsv()

    def loadcsv(self):
        with open('./kelas_2b/toilet_toto.csv') as toto_wekwek:
            read = csv.reader(toto_wekwek, delimiter=',')
            for row in read:
                if row[0] == self.keyword:
                    print("ini linknya: " + row[1])