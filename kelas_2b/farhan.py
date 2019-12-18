import random
import pandas as p


class farhan() :
    game = p.read_csv('kelas_2b/angka.csv')
    
    acak = random.randint(0,3)
    
    temp = game.iloc[acak]
    