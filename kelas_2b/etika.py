import csv

class Hitung:
   def Isi(self):
        self.f = open('kelas_2b/Etika.csv','r')
        self.reader = csv.reader(self.f)
        
        for row in self.reader:
            print ('Jumlah dari %s + %s adalah %s' %(row[0], row[1], float(row[0]) + float(row[1])))

        self.f.close()