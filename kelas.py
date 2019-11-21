class MataUang:
    def __init__(self,idr):
        self.idr = idr

    #idam fadilah - 1184063
    def hongaria_forint(self):
        hasil=self.idr*0.021
        return hasil
    
    #dinda masjesty
    def Anguilla(self, idr):
        hasil = float(idr) * 0.00019
        return hasil

    #tri angga dio simamora
    def Bolivia(self, currency):
        result = float(currency) * 0.00049
        return result