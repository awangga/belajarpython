import csv
import requests 
import matplotlib.pyplot as plt
import sqlite3

class DindaAnik(object):
    def lagu(self):
      with open('kelas_2c/dinda.csv', 'r') as file:
          sic = csv.reader(file, delimiter=',')
          for row in sic:
              print("lagu terpopuler adalah ", row)
    def DindaAnik2(self)  :    
            contacts = []

            with open('kelas_2c/dinda.csv') as csv_file:
              csv_reader = csv.reader(csv_file, delimiter=",")
              for row in csv_reader:
                contacts.append(row)

                print(contacts)

    def DindaAnik3(self)  :
           with open('kelas_2c/dinda.csv', mode='a') as csv_file:
              # membuat objek writer
              writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
              # menulis baris ke file CSV
              writer.writerow(["Memories","Maroon 5","5000000"])
              writer.writerow(["Circles", "Post Malone", "3500000"])

    def judul(self):
        coba = open('kelas_2c/dinda.csv')
        data = csv.reader(coba, delimiter= 'r')
        for row in data:
            print (row)


    def tambah(self):
        file = open('kelas_2c/dinda.csv', 'a', newline='\n')
        lagubaru = [
            ['Kumau Dia'],
            ['Nyaman']
        ]
        filecsv = csv.writer(file)
        filecsv.writerows(lagubaru)
    
        print("Writing Done!")


    def penyanyi(self):
        penyanyi1 = "1"
        penyanyi2 = "2"

        if penyanyi1 == "1":
            print("Juice WRLD")
        elif penyanyi2 == "2":
            print("Billie Elish")
        else:
            print("Penyayi Terpopuler")

    def grafiktanggalagu(self):
        plt.plot([1,2,3,4,5,6,7,8],[87, 90, 95, 93, 85, 86, 90, 97])
        plt.show()

    def request(self):
        req = requests.get('https://www.youtube.com/')
        req.encoding      
        req.status_code   
        req.elapsed       
        req.url           
        req.history  
        req.headers['Content-Type']
        try:
            print(req.status_code)
            print(req.encoding)
            print(req.headers)
            print(req.url)
            print(req.elapsed)
            print(req.history)
        except Exception as e:
            print(e)

    def matpotlib(self):
        x = [1,2,3,4,5,6,7,8,]
        y = [11,12,13,14,15,16,17,18]
        plt.scatter(x,y)
        plt.show()
    def matpotlib1(self):
            x = ([1,2,3,4,5,6,7,8,9],[11,12,13,14,15,16,17,18])
            num_bins = 6
            plt.hist(x,num_bins, facecolor = 'blue')
            plt.title("contoh judul pada matplotlib")
            plt.xlabel("label x matplotlib")
            plt.ylabel("label y matplotlib")

            plt.show()
        
    def start(self):
             self.DindaAnik2()
             self.DindaAnik3()
             self.judul()
             self.tambah()
             self.penyanyi()
             self.grafiktanggalagu()
             self.request()
             self.matpotlib()
             self.matpotlib1()  