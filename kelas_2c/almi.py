import csv

class cs(object):
    def read(self):
        f = open ('kelas_2c/almibachri.csv','r')
        content = [["nama","tlp"]]
        for row in csv.reader(f):
            content.append(row)
            
        for p_row in content:
            for i in range(0,len(p_row),1):
                print(p_row[i], end = ',')
            print("Ini Nomor Customer Service")
            f.close()