import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json 

class Mur:
    def mur(self,npm):
        print("Masukan NPM:")
        if len(npm)<6:
            print("npm kurang dari 6 digit")
        elif len (npm)>7:
            print("npm lebih dari 6 digit")
        else:
            with open('kelas_2c/mur.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    if row[0] == npm:
                        print(row[0], row[1], row[2])
                    else:
                        print("Tidak Ada Data")        
    def mur1(self):
        
       murnia = pd.read_csv('kelas_2c/mur.csv')
       print(murnia)
    
    def muri(self)  :    
            contacts = []

            with open('kelas_2c/mur.csv') as csv_file:
              csv_reader = csv.reader(csv_file, delimiter=",")
              for row in csv_reader:
                contacts.append(row)

            print(contacts)
    def mur2(self)  :
           with open('kelas_2c/mur.csv', mode='a') as csv_file:
              # membuat objek writer
              writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
              # menulis baris ke file CSV
              writer.writerow(["1184003","Dinda","D4 TI 2C"])
              writer.writerow(["1184038", "Nurul", "D4 TI 2C"])
    
           print("Writing Done!")
    def panggil1(self):
     res = requests.get('https://scotch.io')

     print(res)

    def panggil2(self):
        s = requests.session()

        s.get('https://httpbin.org/cookies/set/sessioncookie/1234567')
        r = s.get('https://httpbin.org/cookies')
        print(r.text)
    def panggil3(self):
       payload = {'user_name': 'admin', 'password': 'password'}
       r = requests.post("http://httpbin.org/post", data=payload)
       print(r.url)
       print(r.text)
    def matplotlib(self):
        x=[]
        y=[]

        with open ('kelas_2c/hasil.txt','r') as csvfile:
	        plots = csv.reader(csvfile, delimiter=',')
	        for row in plots:
	            x.append(int(row[0]))
	            y.append(int(row[1]))
	
        plt.plot(x,y, marker='o')
        plt.title('Data Gelombang Otak')
        plt.xlabel('banyak data')
        plt.ylabel('Gelombang Data')
        plt.show()
    def matplotlib2(self):
        x = [1,2,3,4,5,6,7,8,9]
        y = [11,12,13,14,15,16,17,18,19]
        plt.scatter(x,y)
        plt.show()
    def matpotlib3(self):
            x = ([1,2,3,4,5,6,7,8,9],[11,12,13,14,15,16,17,18,19])
            num_bins = 6
            plt.hist(x,num_bins, facecolor = 'green')
            plt.title("contoh judul pada matplotlib")
            plt.xlabel("label x matplotlib")
            plt.ylabel("label y matplotlib")

            plt.show()
        
    def call(self):
             self.mur1()
             self.muri()
             self.mur2()
             self.panggil1()
             self.panggil2()
             self.panggil3()
             self.matplotlib() 
             self.matplotlib2() 
             self.matpotlib3()  