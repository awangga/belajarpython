import csv


class innalkariem(object):
    def lagu(self):
      with open('kelas_2b/innal.csv', 'r') as file:
          sic = csv.reader(file, delimiter=',')
          for row in sic:
              print("lagu terhits adalah ", row)
       
                    
                
                
                
             
                
            
    
