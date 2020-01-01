from selenium import webdriver
import csv
import matplotlib.pyplot as plt
import numpy as np
import requests
import sqlite3
import os

class Dinda(object):
    def CrootKeun(self):
        self.OpenCSV()
        self.CobaMatplotlib()
        self.CobaRequestAPI()
        self.PrintDataAPI()
        self.CobaDatabase()
        self.InsertRecord()
        self.ShowRecord()
        self.ShowBraga()
        self.UpdateRecord()
        self.DeleteRecord()

    def OpenBrowser(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=options)

    def OpenCSV(self):
        self.OpenBrowser()
        with open('kelas_2b/dinda.csv', 'r') as csvfile:
            plot = csv.reader(csvfile, delimiter=',')
            for row in plot:
                print("Informasi Jadwal Bioskop Hari Ini", row[0], row[1], row[2])
                self.driver.get(
                    "https://jadwalnonton.com/bioskop/di-" + row[0] + "/" + row[1] + "-" + row[2] + "-" + row[0] + ".html")
                try:
                    error = self.driver.find_element_by_xpath("//div[contains(@class, 'caution')]").text
                    if "404" in error:
                        print("error")
                except:
                    data = self.driver.find_elements_by_xpath("//div[contains(@class, 'col-sm-10 sched_desc')]")
                    for i in data:
                        var = i.text
                        print(var.strip("LIHAT DI BIOSKOP LAIN"))
                        print("")
            self.driver.close()

    def CobaMatplotlib(self):
        x, y, x1, y1 = np.loadtxt('kelas_2b/dinda_matplotlib.txt', delimiter=',', unpack=True)
        plt.plot(x, y, label='Data Harga Tahun 2019', linewidth=5)
        plt.plot(x1, y1, label='Daftar Harga Tahun 2020', linewidth=5)

        plt.xlabel('Bulan')
        plt.ylabel('Harga Cabe-Cabean/kg')
        plt.title('Grafik Perbandingan Harga Cabe-Cabean Tahun 2019 dan 2020')
        plt.legend()
        plt.savefig("kelas_2b/dinda_matplotlib.png")

    def CobaRequestAPI(self):
        url = "https://nasaapidimasv1.p.rapidapi.com/getEPICEarthImagery"

        payload = ""
        headers = {
            'x-rapidapi-host': "NasaAPIdimasV1.p.rapidapi.com",
            'x-rapidapi-key': "eb2128d0b8msh851eef4aeea9536p1ed7bejsn65c591476041",
            'content-type': "application/x-www-form-urlencoded"
        }

        self.response = requests.request("POST", url, data=payload, headers=headers)
        print(self.response.text)

    def PrintDataAPI(self):
        data = self.response.json()
        for img in data['contextWrites']['to']:
            print(img['image'], img['caption'])

    def CobaDatabase(self):
        self.connection = sqlite3.connect('./kelas_2b/dinda.db')
        self.cursor = self.connection.cursor()

        try:
            self.cursor.execute('CREATE TABLE Bioskop (id INTEGER PRIMARY KEY, Nama_bioskop VARCHAR(100), Kota VARCHAR(100), Mall VARCHAR(100))')
        except:
            print("Tabelnya udah ada!")
    def InsertRecord(self):
        try:
            self.cursor.execute('INSERT INTO Bioskop VALUES(?, ?, ?, ?)', (1, "xxi", "bandung", "btc"))
            self.cursor.execute('INSERT INTO Bioskop VALUES(?, ?, ?, ?)', (2, "xxi", "bandung", "braga"))
            self.cursor.execute('INSERT INTO Bioskop VALUES(?, ?, ?, ?)', (3, "xxi", "bandung", "ciwalk"))
            self.cursor.execute('INSERT INTO Bioskop VALUES(?, ?, ?, ?)', (4, "xxi", "bandung", "empire"))

            self.connection.commit()
        except:
            print("Record sudah ada!")

    def ShowRecord(self):
        self.cursor.execute('SELECT * FROM Bioskop')
        row = self.cursor.fetchall()

        for i in row:
            Nama_Bioskop = i[1]
            Kota = i[2]
            Mall = i[3]

            print("Nama Bioskop : " + str(Nama_Bioskop))
            print("Kota : " + str(Kota))
            print("Mall : " + str(Mall))

        self.connection.commit()

    def ShowBraga(self):
        idBraga = 1
        self.cursor.execute('SELECT * FROM Bioskop WHERE id=?', (idBraga, ))
        row = self.cursor.fetchone()

        print("Nama Bioskop : " + str(row[1]))
        print("Kota : " + str(row[2]))
        print("Mall : " + str(row[3]))

        self.connection.commit()

    def UpdateRecord(self):
        self.cursor.execute('UPDATE Bioskop set Kota =? WHERE id =?', ('Jakarta', 2))
        self.connection.commit()

        self.cursor.execute('SELECT Nama_bioskop, Kota, Mall FROM Bioskop')
        update = self.cursor.fetchall()
        print(update)

    def DeleteRecord(self):
        delete_data = 4
        self.cursor.execute('DELETE FROM Bioskop WHERE id =?', (delete_data, ))
        self.connection.commit()

        self.cursor.execute('SELECT Nama_bioskop, Kota, Mall FROM Bioskop')
        delete = self.cursor.fetchall()
        print(delete)








