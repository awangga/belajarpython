from selenium import webdriver
from time import sleep
import csv



class TriAngga(object):
    def __init__(self, keyword):
        self.keyword = keyword

    def run(self):
        self.openbrowser()

    def openbrowser(self):
        with open('./kelas_2b/toilet_toto.csv') as toto_wekwek:
            read = csv.reader(toto_wekwek, delimiter=',')
            for row in read:
                if row[0] == self.keyword:
                    options = webdriver.ChromeOptions()
                    options.add_argument("--headless")
                    driver = webdriver.Chrome(chrome_options=options)
                    driver.get(row[1])
                    sleep(1)
                    driver.close()