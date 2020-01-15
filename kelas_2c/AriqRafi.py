# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 07:16:35 2020

@author: Asus
"""

import csv
import requests
import matplotlib.pyplot as plt


class Ariq():
    
    def Menu(self):
        self.Salam()
        self.Reader()
        self.List()
        self.Menulis()
        self.Nano()
        self.link()
        self.Line_plot()
        self.Scatter_plot()
        self.Histogram()
    
    #Method file CSV
    def Salam(self):
        print ("PT.Ernakan Indonesia Subur")
    
    def Reader(self):
        with open('kelas_2c/contacts2.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            print(csv_reader)
            for row in csv_reader:
                print(row)
    
    def List(self):
        contacts2 = []

        with open('kelas_2c/contacts2.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                contacts2.append(row)

        labels = contacts2.pop(0)

        #print(labels)

        print(f'{labels[0]} \t {labels[1]} \t\t {labels[2]}')
            
    def Menulis(self):
        with open('kelas_2c/contacts2.csv', mode='a') as csv_file:
            # membuat objek writer
            writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # menulis baris ke file CSV
            writer.writerow(["5", "Dian", "021100022"])
            writer.writerow(["6", "Meli", "0214444432"])
        
            print("Writing Done!")
       
    #Method requests    
    def Nano(self):
        req = requests.post('https://en.wikipedia.org/w/index.php', data = {'search':'Nanotechnology'})
        req.raise_for_status()
        with open('Nanotechnology.html', 'wb') as fd:
            for chunk in req.iter_content(chunk_size=50000):
                fd.write(chunk)
        
    def link(self):
        url = 'https://ariqrafikusumah.blogspot.com/'
        myobj = {'somekey': 'somevalue'}

        x = requests.post(url, data = myobj)

        print(x.text)
    #Method matplotlib.pyplot as plt
    
    def Line_plot(self):
        plt.plot([4,8,13,17,20],[54, 67, 98, 78, 45])
        plt.show()
        
    def Scatter_plot(self):
        x = [2,4,6,7,9,13,19,26,29,31,36,40,48,51,57,67,69,71,78,88]
        y = [54,72,43,2,8,98,109,5,35,28,48,83,94,84,73,11,464,75,200,54]
        plt.scatter(x,y)
        plt.show()
        
    def Histogram(self):
        x = [2,4,6,5,42,543,5,3,73,64,42,97,63,76,63,8,73,97,23,45,56,89,45,3,23,2,5,78,23,56,67,78,8,3,78,34,67,23,324,234,43,544,54,33,223,443,444,234,76,432,233,23,232,243,222,221,254,222,276,300,353,354,387,364,309]
        num_bins = 6
        n, bins, patches = plt.hist(x, num_bins, facecolor = 'green')
        plt.show()