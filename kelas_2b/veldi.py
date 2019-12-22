import csv
class veldi(object):
    def veldi(sef):
        with open('kelas_2b/veldi.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                print(row)