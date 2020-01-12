import csv
import matplotlib.pyplot as plt
import requests
import numpy as np

class Gany(object):
    def Color(self):
        with open('kelas_2c/gany.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            bulann = []
            warnaa = []
            for row in readCSV:
                warna = row[1]
                bulan = row[0]
                bulann.append(bulan)
                warnaa.append(warna)
            
            print(bulann)
            print(warnaa)
    def color2(self):  
            databaru = [
            ['januari', 'biru muda'],
            ['februari', 'totska']   
            ]
            with open('kelas_2c/gany.csv', 'a', newline='') as filecsv:
                datafile = csv.writer(filecsv)
                datafile.writerows(databaru)
    def color3(self):
            # tentukan lokasi file, nama file, dan inisialisasi csv
            f = open('kelas_2c/gany.csv', 'r')
            reader = csv.reader(f)

            # membaca baris per baris
            for row in reader:
                 print (row)

            # menutup file csv
            f.close()

    def matplotlib(self):
        plt.plot([10,7,12,18,15],[55, 68, 99, 74, 43])
        plt.show()

    def matplotlib2(self):
        x = [2,4,6,7,9]
        y = [54,72,43,29,30]
        plt.scatter(x,y)
        plt.show()

    def requests(self):
        req = requests.post('https://en.wikipedia.org/w/index.php', data = {'search':'smile'})
        req.raise_for_status()
        with open('smile.html', 'wb') as fd:
            for chunk in req.iter_content(chunk_size=50000):
                fd.write(chunk)
    def requests2(self):
        req = requests.get('https://upload.wikimedia.org/wikipedia/commons/3/36/Forest_path_and_trees.jpg', stream=True)
        req.raise_for_status()
        with open('Forest.jpg', 'wb') as fd:
            for chunk in req.iter_content(chunk_size=50000):
                print('Received a Chunk')
                fd.write(chunk)

    def requests3(self):
        ssn = requests.Session()
        ssn.cookies.update({'visit-month': 'February'})
 
        reqOne = ssn.get('http://httpbin.org/cookies')
        print(reqOne.text)
        # prints information about "visit-month" cookie
 
        reqTwo = ssn.get('http://httpbin.org/cookies', cookies={'visit-year': '2017'})
        print(reqTwo.text)
        # prints information about "visit-month" and "visit-year" cookie
 
        reqThree = ssn.get('http://httpbin.org/cookies')
        print(reqThree.text)
        # prints information about "visit-month" cookie

    def requests4(self):
        jar = requests.cookies.RequestsCookieJar()
        jar.set('first_cookie', 'first', domain='httpbin.org', path='/cookies')
        jar.set('second_cookie', 'second', domain='httpbin.org', path='/extra')
        jar.set('third_cookie', 'third', domain='httpbin.org', path='/cookies')
 
        url = 'http://httpbin.org/cookies'
        req = requests.get(url, cookies=jar)
 
        req.text
        # returns '{ "cookies": { "first_cookie": "first", "third_cookie": "third" }}'

    def eye(self):
        matrix_two = np.arange(1,10).reshape(3,3)
        matrix_two

    def panggil(self):
        self.Color()
        self.color2()
        self.color3()
        self.matplotlib()
        self.matplotlib2()
        self.requests()
        self.requests2()
        self.requests3()
        self.requests4()
        self.eye()
