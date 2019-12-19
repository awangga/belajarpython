from selenium import webdriver
from time import sleep
import csv



class TriAngga(object):
    def run(self):
        self.openbrowser()

    def openbrowser(self):
        with open('./kelas_2b/toilet_toto.csv') as toto_wekwek:
            read = csv.reader(toto_wekwek, delimiter=',')
            for row in read:
                if row[0] == "spotify":
                    driver = webdriver.Chrome()
                    driver.get(row[1])
                    sleep(2)
                    driver.close()