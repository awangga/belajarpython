import csv

class Kevin(object):
	"""docstring for ClassName"""
	def __init__(self, kode):
		self.kode = kode

	def function(self):
		with open('kelas_2c/Kevin.csv','r') as harga:
			reader = csv.reader(harga)
			for row in reader:
				if str(row[0]) == self.kode:
					print("Kode barang",row[0],"nama barang",row[1],"jumlah",row[2],"harga",row[3])
