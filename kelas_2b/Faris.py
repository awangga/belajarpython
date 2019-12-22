import pandas as bunglon

class farisIhsan:
    def fmi(self, harga):
        print("masukan Harga")
        print(harga)
        
        data = bunglon.read_csv('kelas_2b/Faris.csv')
        print(data)
        print("")
        print("")
        
        print(data[data['Harga'] < harga])
        
        
        print("Filter Berdasarkan: Harga kurang dari " + str(harga))
                