import sqlite3
import csv
import matplotlib.pyplot as plt
import requests
class ryan:
    def awal(self):
        print ("Welcome to jungle")
        
    def gudang(self):
        tes = open('kelas_2c/ryan.csv')
        data = csv.reader(tes, delimiter= 'r')
        for row in data:
            print (row)
            
    def matplotlib(self):
        plt.plot([4,8,13,17,20],[54, 67, 98, 78, 45])
        plt.show()
        
    
    def reqq(self):
        req = requests.get('https://github.com/awangga/belajarpython/')
        req.encoding
        req.status_code
        req.elapsed
        req.url           
        req.history
        req.headers['Content-Type']
    
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

    def matpotlib2(self):
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
    
    def runing(self):
        self.awal()
        self.gudang()
        self.matplotlib()
        self.reqq()
        self.penyanyi()
        self.grafiktanggalagu()
        self.matpotlib2()
        self.matpotlib1()