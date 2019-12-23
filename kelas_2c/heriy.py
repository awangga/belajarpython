import csv

class Anime(object):
    f = open('kelas_2c/manga.csv', 'r')
    reader = csv.reader(f)
    manga = []
    for row in reader:
        manga.append(row)
        
    print("Here are the popular manga in 2019:")
    
    for item in manga:
        print(item)