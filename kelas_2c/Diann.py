# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 21:58:07 2019

@author: ASUS
"""

import csv


class Diann(object):
    def Nama(self):
      with open('kelas_2c/Dian.csv', 'r') as file:
          sic = csv.reader(file, delimiter=',')
          for row in sic:
              print("Atas Nama",row[0], "Bekerja sebagai", row[1], "dan lulusan tahun", row[2])