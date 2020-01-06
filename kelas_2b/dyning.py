import sqlite3
import csv
from selenium import webdriver 
import matplotlib.pyplot as plt
import requests

class Dyning(object):
    def __init__(self, kelas, npm, hari):
        self.kelas = kelas
        self.npm = npm
        self.hari = hari
        
    def angkatan(self):
        if len(str(self.npm)) == 7:
            print(self.npm)
            if self.npm[2] == "8":
                print("Merupakan mahasiswa angkatan 2018")
            elif self.npm[2] == "7":
                print("Merupakan mahasiswa angkatan 2017")
            elif self.npm[2] == "9":
                print("Merupakan mahasiswa angkatan 2019")
            else: 
                print("Merupakan angkatan sebelum 2017")
        else:
            print("cek kembali npm anda")
        

    def jurusan(self):
        if len(self.npm)/2 == 3:
            try:
                if self.npm[0] == "1":
                    print("teknik informatika")
                elif self.npm[0] == "2":
                    print("manajemen informatika")
                elif self.npm[0] == "3":
                    print("manajemen bisnis")
                elif self.npm[0] == "4":
                    print("logistik bisnis")
                else:
                    print("coba cek ke npm lagi")
            except Exception as e:
                print(e)

    def bacacsv(self):
       with open('kelas_2b/dyning.csv', 'r') as jadwal:
            reader = csv.reader(jadwal)
            for row in reader:
                if str(row[0]) == self.hari:
                    if str(row[1]) == self.kelas:
                        if len(str(row[1]))%2 == 0:
                            try:
                                print("jadwal", self.kelas)
                                print("pada hari",row[0], "di kelas", row[1], "ada matkul", row[2],"pada jam", row[3])
                            except Exception as e:
                                print(e)
                                print("coba cek penulisan kelas kembali")
                                
    def db(self):
        koneksi = sqlite3.connect('kelas_2b/dyning.db')
        cursor = koneksi.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS \
                NILAI_MAHASISWA(NPM INTEGER PRIMARY KEY, Nama TEXT, Kelas TEXT, Nilai REAL)')
        tampil = "SELECT * FROM NILAI_MAHASISWA "
        try:
            cursor.execute("INSERT INTO NILAI_MAHASISWA VALUES(1184051,'Alifia Zahra', 'D4TI2B', 91)")
            koneksi.commit()
        except Exception:
            print("Recordnya sudah adaa")
        cursor.execute(tampil)
        results = cursor.fetchall()
        for row in results:
            NPM = row[0]
            Nama = row[1]
            Kelas = row[2]
            Nilai = row[3]
            print ("NPM %s, dengan nama %s, dari kelas %s, nilainya %s" % \
            (NPM, Nama, Kelas, Nilai))

    def nilaismt(self):
        print("nilai tiap semesternya yaitu")
        nilaii = [87, 90, 95, 93, 85, 86, 90, 97]
        x = 1
        for i in nilaii:
            if x < 9 :
                print("Nilai semester",x, "yaitu", i)
                x = x+1
    def rata(self):
        nilaii = [87, 90, 95, 93, 85, 86, 90, 97]
        x = 0
        if x < 9 :
            try:
                print("nilai rata-rata total ialah",(nilaii[1] + nilaii[0] + nilaii[2]+ nilaii[3]+ nilaii[4]+ nilaii[5]+ nilaii[6]+ nilaii[7])/8)
            except Exception as e:
                print(e)
        
    def grafiknilai(self):
        print("Berikut ini merupakan grafik perkembangan nilai tiap semester, tunggu sebentar yaa..")
        try:
            plt.plot([1,2,3,4,5,6,7,8],[87, 90, 95, 93, 85, 86, 90, 97])
            plt.xlabel('Semester')
            plt.ylabel('Nilai')
            plt.title('Grafik Perkembangan rata-rata nilai tiap semester')
            plt.show()
        except Exception as e:
            print(e)
    def reqq(self):
        req = requests.get('https://id.pinterest.com/aidabatrishya/')
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
    def login(self): 
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.driver.get('http://siap.poltekpos.ac.id/siap/besan.depan.php')
        self.driver.find_element_by_name('user_name').send_keys(self.npm)
        self.driver.find_element_by_name('user_pass').send_keys("Dyning2902")
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[2]/table[2]/tbody/tr[1]/td[2]/div/form/input[4]').click()
        self.driver.find_element_by_link_text('Ubah Profil').click()
        self.nomer = self.driver.find_element_by_xpath("//input[@name='Handphone']")
        self.nomers = self.nomer.get_attribute('value')
        print("Nomor telepon mahasiwa dengan NPM ", self.npm, "ialah", self.nomers)
        self.driver.close()
    def jalan(self):
        print("Dengan NPM")
        self.angkatan()
        self.jurusan()
        self.bacacsv()
        self.db()
        self.nilaismt()
        self.rata()
        self.reqq()
        self.login()
        self.grafiknilai()
    