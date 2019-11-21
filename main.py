import kelas


nilai=input("masukan nilai idr :")
valueidr=float(nilai)
mataUang = kelas.MataUang(valueidr)

idr = 10000000

#idam fadilah - 1184063
print("Hongaria - forint ",mataUang.hongaria_forint())

#dinda masjesty
mataUang = kelas.MataUang(valueidr)
print(str(mataUang.Anguilla(idr)) + " Dollar Karibean Timur")

#tri angga dio simamora
matUang = kelas.MataUang(valueidr)
matUangconvert = str(matUang.Bolivia(idr)) + " Bolivian Boliviano"
print(matUangconvert)