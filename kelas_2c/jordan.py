# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 17:08:22 2019

@author: Joey
"""
import csv

class Jordan(object):

    def tampil(self):
        try:
            f = open('kelas_2c/jordan.csv', 'r')
            reader = csv.reader(f)
            for row in reader:
                        print (row)
            f.close()
        except:
            print ("Terjadi kesalahan")
        
    def tambahbaris(self):
        f = open('kelas_2c/jordan.csv', 'a')
        barisbaru = [
        ['27', 'aa', 'tampan dan berani']
        ]
        filecsv = csv.writer(f)
        filecsv.writerows(barisbaru)
        
    def buat(self):
        siswa = [
    ('arslan', 'A', 90),
    ('bayu', 'B', 85),
    ('niko', 'A', 80),
    ('abdul', 'B', 90),
    ('dahlan', 'C', 70)
    ]
        f = open('kelas_2c/siswa.csv', 'w')
        w = csv.writer(f)
        w.writerow(('Nama','Kelas','Nilai'))
        for s in siswa:
            w.writerow(s)
        f.close()
        
   