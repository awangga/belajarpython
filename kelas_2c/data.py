# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 21:24:13 2019

@author: USER
"""

import csv

class Nuha(object):
    def __init__ (self, nama):
        self.nama = nama
        
    def NuhaHanifatul(self):
        with open('kelas_2c/data.csv','r') as data:
            reader = csv.reader(data)
            for row in reader:
                if str(row[0]) == self.nama:
                    print("Nama Peminjam", row[0], "meminjam dengan judul", row[2])