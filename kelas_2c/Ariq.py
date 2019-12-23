import csv

class Ariq(object):
	def __init__(self,absen):
		self.absen = absen

	def function(self):
		with open('kelas_2c/Ariq.csv', 'r') as npm:
			reader = csv.reader(npm)
			for row in reader:
				if str(row[0]) == self.absen:
					print("Absen",row[0],"dengan nama",row[1],"kelas",row[2],"dengan npm",row[3])