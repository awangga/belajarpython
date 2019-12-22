# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 17:33:13 2019

@author: Ahmad Agung Tawakkal
"""

import csv

class Tawa(object):
    def Color(self):
        with open('agung.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            dates = []
            colors = []
            for row in readCSV:
                color = row[3]
                date = row[0]
            
                dates.append(date)
                colors.append(color)
            
            print(dates)
            print(colors)
            
            whatColor = input('What color do you wish to know the date of?:')
            coldex = colors.index(whatColor)
            theDate = dates[coldex]
            print('The date of',whatColor,'is:',theDate)