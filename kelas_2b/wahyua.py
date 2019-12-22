import csv

class Umur(object):
    with open('kelas_2b/wahyu.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            print(row)