import pandas as pd
import csv

class rayprastya(object):
    def convert(self):
        read_file = pd.read_csv (r'D:\TI\belajarpython\kelas_2b\dinda.csv')
        read_file.to_excel (r'D:\TI\belajarpython\kelas_2b\dinda.xlsx', index = None, header=True)