import csv


class Jadwal(object):
    with open('bahannya/adit.csv', 'r') as csvfile:
        tumang = csv.reader(csvfile, delimiter=',')
        for row in tumang:
            print("Informasi jadwal Kereta :", row[0], row[1], row[2])
