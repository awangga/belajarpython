import csv
import matplotlib.pyplot as plt
import numpy as np 
import time
import os
import sqlite3
import requests

class fina:

	def manggil(self):
		self.dunia()
		self.tunjuk()
		self.matplotlib()
		self.Req()
		self.Req2()
		self.iniTabel()
		self.masukData()
		self.hapusdata()
		self.array()
		self.time()

	def dunia(self):
		with open('kelas_2c/fina.csv') as file:
			baca = csv.reader(file, delimiter=',')
			for r in baca:
				if int(r[1]) <= 500:
					print ("Negara Di Dunia",(r[2]),(r[3]))
				else:
					print ("Data Lengkap Coy",(r[2]),(r[3]))

	def tunjuk(self):						
		file = open('kelas_2c/fina.csv', 'a', newline='\n')
		barisbaru = [
		    [
		    '1000', '300', 'Haluland','Maju','1300'],
		    ['1000', '210','Haliland','Berkembang','1210']
		]
		filecsv = csv.writer(file)
		filecsv.writerows(barisbaru)

	def matplotlib(self):
		t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
		plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
		plt.savefig("kelas_2c/fina_Matplotlib.png")
		plt.show()
#requsts
	def Req(self):
		i = requests.get('https://github.com/cdwadwdawddawwdawadd')
		print(i.status_code)
		if i:
			print('Istirahat yang cukup')
		else:
			print('Yuhu Ini salah')

	def Req2(self):
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

#Masih coba DataBase
	def iniTabel(self):
		try:
			self.connection = sqlite3.connect('./kelas_2c/fina.db')
			self.cursor = self.connection.cursor()
			self.cursor.execute('CREATE TABLE fina (id INTEGER PRIMARY KEY, nilai VARCHAR(50), tingkat VARCHAR(50), nama VARCHAR(50), jenis VARCHAR(50), value2 VARCHAR(50))')
		except:
			print("Liat lagi yang bener!")

	def masukData(self):
		try:
			self.cursor.execute('INSERT INTO fina VALUES(?, ?, ?, ?, ?)', (1, "1000", "200", "indonesia", "berkembang", "1200"))
			self.cursor.execute('INSERT INTO fina VALUES(?, ?, ?, ?, ?)', (2, "1000", "300", "india", "berkembang", "1300"))
			self.cursor.execute('INSERT INTO fina VALUES(?, ?, ?, ?, ?)', (3, "1000", "500", "jepang", "maju", "1500"))
			self.cursor.execute('INSERT INTO fina VALUES(?, ?, ?, ?, ?)', (3, "1000", "740", "Amerika", "adikuasa", "1740"))
			self.cursor.execute('INSERT INTO fina VALUES(?, ?, ?, ?, ?)', (3, "1000", "120", "Vietnam", "berkembang" , "1120"))
			self.connection.commit()

		except:
			print("Liat Liat Lagi lah!")

	def hapusdata(self):
		db = sqlite3.connect('kelas_2c/fina.db')
		cursor = db.cursor()
		cursor.execute('DELETE FROM fina WHERE value2=1200')
		db.commit()
		print("{} data ini sudah dihapus, thanks next !".format(cursor.rowcount))

#Fungsi Aray	
	def array(self):
		x = np.array([[1,2], [3,4]])
		print(x)
		v = np.array([1,2,3])
		print(v)
		print(v.T) 

	def time(self):
		result = open('kelas_2c/fina.txt','r')
		result = time.localtime()
		print("result:", result)
		print("\nyear:", result.tm_year)
		print("tm_hour:", result.tm_hour)