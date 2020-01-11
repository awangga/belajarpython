import csv
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import requests

class cs(object):
    def read(self):
        f = open ('D:\kelas2c\\bachri.csv','r')
        content = [["nama","tlp"]]
        for row in csv.reader(f):
            content.append(row)
            
        for p_row in content:
            for i in range(0,len(p_row),1):
                print(p_row[i], end = ',')
            print("Ini Nomor Customer Service")
            f.close()
    csv_filename = 'almibachri.csv'
            
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show(self):
        print("=== DATA ===")
        print("[1] Lihat Daftar Mahasiswa")
        print("[2] Buat Absen Baru")
        print("[3] Edit Mahasiswa")
        print("[4] Hapus Absen")
        print("[5] Cari Mahasiswa")
        print("[0] Exit")
        print("------------------------")
        selected_menu = input("Pilih menu> ")
    
        if(selected_menu == "1"):
            show_contact()
        elif(selected_menu == "2"):
            create_contact()
        elif(selected_menu == "3"):
            edit_contact()
        elif(selected_menu == "4"):
            delete_contact()
        elif(selected_menu == "5"):
            search_concat()
        elif(selected_menu == "0"):
            exit()
        else:
            print("Kamu memilih menu yang salah!")
        back_to_menu()

    def back_to_menu(self):
        print("\n")
        input("Tekan Enter untuk kembali...")
        show_menu()
        
    def baca(self):
        with open('almibachri.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            print(csv_reader)
            for data in csv_reader:
                print(data)
    
    def tambah(self):        
        almibachri = []
    with open('almibachri.csv', mode='a') as csv_file:
    # membuat objek writer
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # menulis baris ke file CSV
        writer.writerow(["6", "bnpb", "118"])
        writer.writerow(["7", "pmi", "119"])
    print("Writing Done!")
    
    def tambah_baris_kontak(self):
        with open('almibachri.csv', mode='a') as csv_file:
    # menentukan label
            fieldnames = ['NO', 'NAMA', 'TELEPON']
    
    # membuat objek writer
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # menulis baris ke file CSV
        writer.writeheader()
        writer.writerow({'NO': '8', 'NAMA': 'rumah sakit', 'TELEPON': '210'})
        writer.writerow({'NO': '9', 'NAMA': 'ambulance', 'TELEPON': '211'})    
    print("Writing Done!")
    
    def grafik(self):
        angles = np.arange(0, 3*np.pi, 0.1) # prepare axis data
        sindata = np.sin(angles)
        cosdata = np.cos(angles)
        fig, ax = plt.subplots()
        line1, = ax.plot([], [], color='g')
        line2, = ax.plot([], [], color='r')
        ax.axis([0, 3 * np.pi, -1, 1]) # siapkan rentang sumbu x dan y
        plt.title('Animasi gelombang sinus dan cosinus\n') # judul grafik
        plt.xlabel('Sudut (radian)') # judul sumbu x
        plt.ylabel('Sinus') # judul sumbu y
        plt.grid(True, which='both') # tampilkan grid/kotak-kotak
        def update(num, line1, line2):
            line1.set_data(angles[:num], sindata[:num])
            line2.set_data(angles[:num], cosdata[:num])
            return line1,line2
            ani = animation.FuncAnimation(fig, update, fargs=[line1,line2],interval=10)
            ani.save('gifs/sinecos.gif', writer='imagemagick', fps=30)

    def rikues(self):
        req = requests.get('https://www.youtube.com/results?search_query=cara+bikin+requests+di+python')
 
        req.encoding # returns 'utf-8'
        req.status_code # returns 200
        req.elapsed # returns datetime.timedelta(0, 1, 666890)
        req.url # returns 'https://edureka.co/'
        
        req.history 
        # returns [&lt;Response [301]&gt;, &lt;Response [301]&gt;]
 
        req.headers['Content-Type']
        
