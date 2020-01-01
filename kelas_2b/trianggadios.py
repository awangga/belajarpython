from selenium import webdriver
from time import sleep
import requests
import sqlite3
import csv
import matplotlib.pyplot as plt


class TriAngga(object):
    def __init__(self, npm, keyword):
        self.npm = npm
        self.keyword = keyword
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=self.options)

    def run(self):
        self.openBrowser(self.openCsv())
        self.ambilFoto()
        self.downloadFoto()
        self.buatTabel()
        self.masukinData()
        self.tampilData()
        self.plotCrot()
        self.showGoogle()
        self.updateDatabase()

    def openBrowser(self, keywords):
        self.driver.get(keywords)
        sleep(1)
        self.driver.close()

    def openCsv(self):
        with open('./kelas_2b/toilet_toto.csv') as toto_wekwek:
            read = csv.reader(toto_wekwek, delimiter=',')
            for row in read:
                if row[0] == self.keyword:
                    return row[1]

    def ambilFoto(self):
        self.req = requests.get('https://raw.githubusercontent.com/D4TI/2018/master/kecil/' + self.npm + '.jpg')

    def downloadFoto(self):
        with open(self.npm + '.jpg', 'wb') as download:
            download.write(self.req.content)

    def buatTabel(self):
        try:
            self.connection = sqlite3.connect('./kelas_2b/data_toto.db')
            self.cursor = self.connection.cursor()

            self.cursor.execute('CREATE TABLE wekwek (id INTEGER PRIMARY KEY, keywords VARCHAR(100), link VARCHAR(100))')
        except:
            print("Sudah ada!")

    def masukinData(self):
        try:
            self.cursor.execute('INSERT INTO wekwek VALUES(?, ?, ?)', (1, "youtube", "https://www.youtube.com/"))
            self.cursor.execute('INSERT INTO wekwek VALUES(?, ?, ?)', (2, "google", "https://www.google.com/"))
            self.cursor.execute('INSERT INTO wekwek VALUES(?, ?, ?)', (3, "facebook", "https://www.facebook.com/"))

            self.connection.commit()
        except:
            print("Sudah ada!")

    def tampilData(self):
        self.cursor.execute('SELECT * FROM wekwek')
        row = self.cursor.fetchone()

        keywords = row[1]
        link = row[2]

        print("keywords : " + str(keywords))
        print("link : " + str(link))

        self.connection.commit()

    def plotCrot(self):
        names = [
            "Google",
            "Youtube",
            "Facebook"
        ]

        values = [
            77860000000,
            28440000000,
            23400000000
        ]

        plt.bar(names, values)
        plt.savefig("kelas_2b/dodol_garut.png")

    def showGoogle(self):
        self.cursor.execute('SELECT * FROM wekwek WHERE keywords=?', ("google",))
        row = self.cursor.fetchone()

        print("id : " + str(row[0]))
        print("keywords : " + str(row[1]))
        print("link : " + str(row[2]))

        self.connection.commit()

    def updateDatabase(self):
        self.cursor.execute('UPDATE wekwek set keywords=?, link=? WHERE id =?', ("github", "https://github.com/", 1))
        self.connection.commit()