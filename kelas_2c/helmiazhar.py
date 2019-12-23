# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 19:08:20 2019

@author: Asus
"""
import csv

class helmi:
    def stok(self):
        tes = open('kelas_2c/stok.csv')
        data = csv.reader(tes, delimiter= 'r')
        for row in data:
            print (row)

 
