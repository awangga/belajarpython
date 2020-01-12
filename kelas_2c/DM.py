kode="P1A"
hargatotal= 800000
kuota =5
import matplotlib.pyplot as plt
import requests
import csv

if (kode[1]) == "1":
    print("Avanza", "Innova", "APV")
elif kode[1] == "2":
    print("Xenia", "Yaris", "Jeep")
elif kode[1] == "3":
    print("Mobilio", "Hiace")
elif kode[1] == "4":
    print("Brio", "Camry")
else:
    print("Mobil tidak tersedia")
       
if (kode[0]) =="P":
    print("Mobil BerAC depan belakang")
elif (kode[0]) =="Q":
    print("Mobil BerAC depan saja")
    
if (kode[0]) =="A":
    print("Mobil tersedia 2 per harinya")
elif (kode[2]) =="B":
    print("Mobil tersedia 3 per harinya")
elif (kode[0]) =="C":
    print("Mobil tersedia 4 per harinya")
else:
    print("Mobil tersedia 5 per harinya")
    
if hargatotal > 500000 :
    try:
        print("mendapat potongan harga 5%")
    except Exception :
        print(Exception)
        
if kuota > 4 :
    print (" kuota sudah melebihi")
    if (kode[0]) =="P":
        print ("Wajib asuransi")
    else:
        print ("Tidak perlu asuransi")
    if (kode[0]) =="Q":
        print ("wajib mendapat izin beroperasi")
    else:
        print ("tidak wajib mendapat izin beroperasi")
else:
    print (" belum melebihi")
    
with open('Dianm.csv') as files:
                reader=csv.reader(files,  delimiter=',')
                for row in reader:
                    if (kode[1]) == "1":
                        print("Avanza", "Innova", "APV")
                    elif kode[1] == "2":
                        print("Xenia", "Yaris", "Jeep")
                    elif kode[1] == "3":
                        print("Mobilio", "Hiace")
                    elif kode[1] == "4":
                        print("Brio", "Camry")
                    else:
                        print("Mobil tidak tersedia") 
    
plt.plot([1,2,3,4,5,6,7,8,9,10,11,12],[65, 55, 75, 70, 95, 90, 85, 80, 75, 60, 55, 95])
plt.show()

req = requests.get('https://github.com/dianmarkuci')
req.encoding      
req.status_code   
req.elapsed       
req.url           
req.history  
req.headers['Content-Type']
try:
    print(req.status_code)
    print(req.encoding)
    print(req.headers)
    print(req.url)
    print(req.elapsed)
    print(req.history)
except Exception as e:
    print(e)
    
