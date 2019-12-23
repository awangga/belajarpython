import csv


class DindaAnik(object):
    def lagu(self):
      with open('kelas_2c/dinda.csv', 'r') as file:
          sic = csv.reader(file, delimiter=',')
          for row in sic:
              print("lagu terpopuler adalah ", row)
       
                    
                
                
                
             
                
            
    
