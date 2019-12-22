# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 19:28:24 2019

@author: acer
"""

import csv

class Alifia_Zahra():
    def __init__(self, mobil):
        self.mobil = mobil
        
    def Alifia(self):
        with open ('kelas_2b/alifia.csv', 'r') as rental_mobil:
            reader = csv.reader(rental_mobil, delimiter=',')
            for row in reader:
                if str(row[1]) == self.mobil:
                    print("mobil tipe",row[2], "dapat dirental seharga: ",row[3])
                    
                