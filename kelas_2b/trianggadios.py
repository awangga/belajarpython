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
                    options.binary_location = '/usr/bin/chromium-browser'
                    options.add_argument("--no-sandbox")
                    options.add_argument("--no-default-browser-check")
                    options.add_argument("--no-first-run")
                    options.add_argument("--disable-default-apps")
                    driver = webdriver.Chrome('/home/travis/virtualenv/python3.6/chromedriver',chrome_options=options)
                    driver.get(row[1])
                    sleep(1)
                    driver.close()