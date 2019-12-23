# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 18:18:57 2019

@author: Alfandra's Life
"""

import csv

class dicky(object):
    def karyawanterbaik(self):    
        with open('dicky.txt', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Nama column adalah {", ".join(row)}')
                line_count += 1
                print(row[1],"bekerja dibagin",row[2],",adalah karyawan terbaik bulan",row[3])
                line_count += 1
                print(f'Processed {line_count} lines.')
    
