import csv

class Adit(object):
	"""docstring for ClassName"""
	def __init__(self, nomor):
		self.nomor = nomor

	def function(self):
		with open('kelas_2c/Adit.csv', 'r') as gaji:
			reader = csv.reader(gaji)
			for row in reader:
				if str(row[0]) == self.nomor:
					print("akldnflkas",row[0],"askdniad",row[1],"asdjaosid",row[2],"aisjdioas",row[3],"aksdna",row[4])