# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 17:21:10 2019

@author: NISA
"""

import csv

class Annisa_Khairani():
    def __init__(self, motor):
        self.motor = motor
        
    def Annisa(self):
        with open ('kelas_2c/AnnisaK.csv', 'r') as penjualan:
            reader = csv.reader(penjualan)
            for row in reader:
                    print(row)