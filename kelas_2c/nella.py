# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 14:46:38 2019

@author: Putri Nella
"""

import csv

class nella(object):
    def __init__ (self, paket):
        self.paket = paket


    def PutriNella(self):
        with open('kelas_2c/nella.csv','r') as harga:
            reader = csv.reader(harga)
            for row in reader:
                if str (row[0]) == self.paket:
                    print("pada", row[0], "hari", row[1], "harganya", row[2])
                