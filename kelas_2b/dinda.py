from selenium import webdriver
import csv

class Start(object):

    def OpenBrowser(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome("/home/travis/virtualenv/python3.6.7/bin/chromedriver", chrome_options=options)

        with open('kelas_2b/dinda.csv', 'r') as csvfile:
            plot = csv.reader(csvfile, delimiter=',')
            for row in plot:
                print("Informasi jadwal film bioskop hari ini:", row[0], row[1], row[2])
                self.driver.get("https://jadwalnonton.com/bioskop/di-" + row[0] + "/" + row[1] +"-" + row[2] +"-" + row[0] + ".html")

                try:
                    error = self.driver.find_element_by_xpath("//div[contains(@class, 'caution')]").text
                    if "404" in error:
                        print("error")
                except:
                    jum = self.driver.find_elements_by_xpath("//div[contains(@class, 'col-sm-10 sched_desc')]")
                    for i in jum:
                        var = i.text
                        print(var.strip("LIHAT DI BIOSKOP LAIN"))
                        print("")

        self.driver.close()