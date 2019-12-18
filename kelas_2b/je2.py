import csv
import operator
class jefri:
    def sort(self):
        sample = open('kelas_2b/sort.csv','r')


        sort = sorted(sample,key=operator.itemgetter(0) )

        for eachline in sort:
            print (eachline)