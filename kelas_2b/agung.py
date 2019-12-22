# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 17:33:13 2019

@author: Ahmad Agung Tawakkal
"""

import csv

class Tawa(object):
    def Color(self):
        with open('./kelas_2b/agung.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            bulann = []
            warnaa = []
            for row in readCSV:
                warna = row[1]
                bulan = row[0]
                bulann.append(bulan)
                warnaa.append(warna)
            
            print(bulann)
            print(warnaa)
