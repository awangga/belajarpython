# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 17:08:22 2019

@author: Joey
"""
import csv
import os
import matplotlib.pyplot as plt
import numpy as np
import requests

class Yusuf():

    csv_filename = 'kelas_2c/contacts.csv'
    
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_menu():
        Yusuf.clear_screen()
        print("=== Silahkan Pilih Method Yang di inginkan ===")
        print("[1] Lihat Daftar Kotak")
        print("[2] Buat Kontak Baru")
        print("[3] Edit Kontak")
        print("[4] Hapus Kontak")
        print("[5] Cari Kontak")
        print("[6] Buat Graphic")
        print("[7] Download html")
        print("[0] Exit")
        print("------------------------")
        selected_menu = input("Pilih menu> ")
        
        if(selected_menu == "1"):
            Yusuf.show_contact()
        elif(selected_menu == "2"):
            Yusuf.create_contact()
        elif(selected_menu == "3"):
            Yusuf.edit_contact()
        elif(selected_menu == "4"):
            Yusuf.delete_contact()
        elif(selected_menu == "5"):
            Yusuf.search_contact()
        elif(selected_menu == "6"):
            Yusuf.buat_graphic()
        elif(selected_menu == "7"):
            Yusuf.download_html()
            
        elif(selected_menu == "0"):
            exit()
        else:
            print("Kamu memilih menu yang salah!")
            Yusuf.back_to_menu()
    
    def back_to_menu():
        print("\n")
        input("Tekan Enter untuk kembali...")
        Yusuf.show_menu()
    
    
    def show_contact():
        Yusuf.clear_screen()
        contacts = []
        with open(Yusuf.csv_filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                contacts.append(row)
    
        if (len(contacts) > 0):
            labels = contacts.pop(0)
            print(f"{labels[0]} \t {labels[1]} \t\t {labels[2]}")
            print("-"*34)
            for data in contacts:
                print(f'{data[0]} \t {data[1]} \t {data[2]}')
        else:
            print("Tidak ada data!")
        Yusuf.back_to_menu()
    
    
    def create_contact():
        Yusuf.clear_screen()
        with open(Yusuf.csv_filename, mode='a') as csv_file:
            fieldnames = ['NO', 'NAMA', 'TELEPON']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            no = input("No urut: ")
            nama = input("Nama lengkap: ")
            telepon = input("No. Telepon: ")
    
            writer.writerow({'NO': no, 'NAMA': nama, 'TELEPON': telepon})
            print("Berhasil disimpan!")
    
        Yusuf.back_to_menu()
    
    
    def search_contact():
        Yusuf.clear_screen()
        contacts = []
    
        with open(Yusuf.csv_filename, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                contacts.append(row)
    
        no = input("Cari berdasrakan nomer urut> ")
    
        data_found = []
    
        # mencari contact
        indeks = 0
        for data in contacts:
            if (data['NO'] == no):
                data_found = contacts[indeks]
                
            indeks = indeks + 1
    
        if len(data_found) > 0:
            print("DATA DITEMUKAN: ")
            print(f"Nama: {data_found['NAMA']}")
            print(f"Telepon: {data_found['TELEPON']}")
        else:
            print("Tidak ada data ditemukan")
        Yusuf.back_to_menu()
        
    
    
    def edit_contact():
        Yusuf.clear_screen()
        contacts = []
    
        with open(Yusuf.csv_filename, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                contacts.append(row)
    
        print("NO \t NAMA \t\t TELEPON")
        print("-" * 32)
    
        for data in contacts:
            print(f"{data['NO']} \t {data['NAMA']} \t {data['TELEPON']}")
    
        print("-----------------------")
        no = input("Pilih nomer kontak> ")
        nama = input("nama baru: ")
        telepon = input("nomer telepon baru: ")
    
        # mencari contact dan mengubah datanya
        # dengan data yang baru
        indeks = 0
        for data in contacts:
            if (data['NO'] == no):
                contacts[indeks]['NAMA'] = nama
                contacts[indeks]['TELEPON'] = telepon
            indeks = indeks + 1
    
        # Menulis data baru ke file CSV (tulis ulang)
        with open(Yusuf.csv_filename, mode="w") as csv_file:
            fieldnames = ['NO', 'NAMA', 'TELEPON']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for new_data in contacts:
                writer.writerow({'NO': new_data['NO'], 'NAMA': new_data['NAMA'], 'TELEPON': new_data['TELEPON']}) 
    
        Yusuf.back_to_menu()
    
    
    
    def delete_contact():
        Yusuf.clear_screen()
        contacts = []
    
        with open(Yusuf.csv_filename, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                contacts.append(row)
    
        print("NO \t NAMA \t\t TELEPON")
        print("-" * 32)
    
        for data in contacts:
            print(f"{data['NO']} \t {data['NAMA']} \t {data['TELEPON']}")
    
        print("-----------------------")
        no = input("Hapus nomer> ")
    
        # mencari contact dan mengubah datanya
        # dengan data yang baru
        indeks = 0
        for data in contacts:
            if (data['NO'] == no):
                contacts.remove(contacts[indeks])
            indeks = indeks + 1
    
        # Menulis data baru ke file CSV (tulis ulang)
        with open(Yusuf.csv_filename, mode="w") as csv_file:
            fieldnames = ['NO', 'NAMA', 'TELEPON']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for new_data in contacts:
                writer.writerow({'NO': new_data['NO'], 'NAMA': new_data['NAMA'], 'TELEPON': new_data['TELEPON']}) 
    
        print("Data sudah terhapus")
        Yusuf.back_to_menu()
        
        
    def buat_graphic():
        Yusuf.clear_screen()
        x = np.linspace(0,10,10)
        y = x * x
        y2 = y * x
        try: 
            plt.title("Grafik Sederhana")
            plt.xlabel("Sumbu X")
            plt.ylabel("Sumbu Y")
            plt.plot(x,label="x")
            plt.plot(y,label="y")
            plt.plot(y2,label="y2")
            plt.legend()
            plt.show()
            Yusuf.back_to_menu
        except Exception as a:
            print(a)
            print("Cek Angka")
            
        
    def download_html():
        Yusuf.clear_screen()
        req = requests.post('https://en.wikipedia.org/w/index.php', data = {'search':'Nanotechnology'})
        req.raise_for_status()
        try:
            with open('Nanotechnology.html', 'wb') as fd:
                for chunk in req.iter_content(chunk_size=50000):
                    fd.write(chunk)
            Yusuf.back_to_menu
        except Exception as e:
            print(e)
            print("Not Found 404")
            
