import csv
	
class fina:

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
		    ['1000', '300', 'Haluland','Maju','1300'],
		    ['1000', '210','Haliland','Berkembang','1210']
		]
		filecsv = csv.writer(file)
		filecsv.writerows(barisbaru)