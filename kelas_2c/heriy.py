import csv
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
import sqlite3
import requests

class heriy:
    
    def fairytail(self):
        with open('./kelas_2c/anime.csv', mode='a') as csv_file:
            fieldnames = ['NO', 'JUDUL', 'TERJUAL']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            writer.writerow({'NO': '5', 'JUDUL': 'Haikyuu', 'TERJUAL': '1500000'})
            writer.writerow({'NO': '6', 'JUDUL': 'Oresuki', 'TERJUAL': '1000000'})
        
        print("Writing Done!")
    
    def onepiece(self):
        with open('./kelas_2c/anime.csv') as csv_file:
            anime = csv.DictReader(csv_file)
            for anim in anime:
                if int(anim['TERJUAL']) >= 5000000:
                    print(anim['JUDUL'], " Anime ini akan mendapatkan season baru")
                else:
                    print(anim['JUDUL'], " Anime ini tidak mendapatkan season baru")
    
    def naruto(self):
        anime = []
        
        with open('./kelas_2c/anime.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for anim in csv_reader:
                anime.append(anim)
        
        print("NO \t JUDUL \t\t TERJUAL")
        print("-" * 32)
        
        for data in anime:
            print(f"{data['NO']} \t {data['JUDUL']} \t {data['TERJUAL']}")
    
    def bleach(self):
        plt.style.use('fivethirtyeight')
        
        Anime = ["Neverland","Demon Slayer","Fairy Tail", "Naruto","One Piece"]
        
        Views = [3849600,4200000,6231600,6731700,7375200]
        plt.plot(Anime, Views, color='k', linestyle='--', marker='.', label='Viewer')
        
        reads = [4537200,5385000,7000000,7149600,7537000]
        plt.plot(Anime, reads, color='b', label='Reader')
        
        disc = [4351500,4929300,3781000,5637300,5343700]
        plt.plot(Anime, disc, color='#adad3b', label='Disclaimer')
        
        plt.xlabel('Title Anime')
        plt.ylabel('Total Views')
        plt.title('Views Anime in Year 2019')
        
        plt.legend()
        plt.grid(True)
        plt.savefig('anime.png')
        
        plt.show()
        
    def demon(self):
        style.use('ggplot')
        
        x,y = np.loadtxt('./kelas_2c/anime1.csv', unpack = True, delimiter = ',')

        plt.plot(x,y)

        plt.title('Epic Chart')
        plt.ylabel('Y ax')
        plt.xlabel('X ax')

        plt.show()
        
    def oresuki(self):
        try:
            self.conn = sqlite3.connect('./kelas_2c/anime.db')
            self.c = self.conn.cursor()
        except:
            print("Anime None")
     
    def oresuki1(self):
        try:
            self.c.execute('CREATE TABLE IF NOT EXISTS anim (kode REAL, datestamp TEXT, judul TEXT, terjual TEXT)')
        except:
            print("Anime none")
    
    def oresuki2(self):
        try:
            self.c.execute("INSERT INTO anim VALUES(1, '2019-01-02', 'One Piece', '7000000')")
            self.c.execute("INSERT INTO anim VALUES(2, '2019-01-02', 'Fairy Tail', '6000000')")
            self.c.execute("INSERT INTO anim VALUES(3, '2019-01-02', 'Naruto', '5000000')")
            self.c.execute("INSERT INTO anim VALUES(4, '2019-01-02', 'Kingdom', '4500000')")
            self.conn.commit()
        except:
            print("Anime None")
    
    def oresuki3(self):
        try:
            self.c.execute('SELECT * FROM anim')
            [print(row) for row in self.c.fetchall()]
            
            self.c.execute("UPDATE anim SET terjual = '4000000' WHERE terjual = '4500000'")
            self.conn.commit()
            
            self.c.execute('SELECT * FROM anim')
            [print(row) for row in self.c.fetchall()]
        except:
            print("Anime None")
    
    def oresuki4(self):
        try:
            self.c.execute('SELECT * FROM anim')
            [print(row) for row in self.c.fetchall()]
            
            self.c.execute('DELETE FROM anim WHERE id = 4')
            self.conn.commit()
            
            self.c.execute('SELECT * FROM anim')
            [print(row) for row in self.c.fetchall()]
        except:
            print("Anime None")
    
    def nisekoi(self):
        r = requests.get('http://animekompi.web.id/')
        print(r.text)
    
    def nisha(self):
        b = requests.get('https://elwiki.net/wiki/images/e/e4/Portrait_-_Nisha_Labyrinth_%28Awakening%29.png')
        
        with open('nisha.png', 'wb') as f:
            f.write(b.content)
            
    def japan(self):
        self.fairytail()
        self.onepiece()
        self.naruto()
        self.bleach()
        self.demon()
        self.oresuki()
        self.oresuki1()
        self.oresuki2()
        self.oresuki3()
        self.oresuki4()
        self.nisekoi()
        self.nisha()