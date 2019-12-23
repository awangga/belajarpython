# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 21:09:56 2019

@author: Dell
"""

import csv

class Bioskop(object):
    
    #lokasi file dan nama csv yang telah disimpan
    with open('kelas_2c/ayu.csv') as csvfile:
        
        #untuk membaca dan  menampilkan semua data yang ada di file
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            print(row)