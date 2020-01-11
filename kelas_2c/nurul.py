import csv
import matplotlib.pyplot as plt
import requests

class nurul:

    def ganjilgenap(self):
        with open('kelas_2c/nurul.csv') as files:
            reader=csv.reader(files,  delimiter=',')
            for row in reader:
                if int(row[0])%2 == 1:
                    print(row[0],"merupakan Bilangan Ganjil")
                else:
                    print(row[0],"merupakan Bilangan Genap atau Bukan Bilangan Ganjil")
                
    def urutan(self):
        contacts = []

        with open('kelas_2c/nurul.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
             contacts.append(row)


        labels = contacts.pop(0)

        #print(labels)
        #print(contacts)

        print("-"*34)
        print(f'{labels[0]}')
        for data in contacts:
         print("-"*34)
         print(f'{data[0]}')

    def tambah(self):
        file = open('kelas_2c/nurul.csv', 'a', newline='\n')
        barisbaru = [
            ['21'],
            ['22']
        ]
        filecsv = csv.writer(file)
        filecsv.writerows(barisbaru)
    
        print("Writing Done!")

    def metplot(self):
       plt.plot([1, 2, 3, 4])
       plt.ylabel('some numbers')
       plt.show()

    def acak(self):
        x = [2,4,6,7,9,13,19,26,29,31,36,40,48,51,57,67,69,71,78,88]
        y = [54,72,43,2,8,98,109,5,35,28,48,83,94,84,73,11,464,75,200,54]
        plt.scatter(x,y)
        plt.show()

    def histogram(self):
        x = [2,4,6,5,42,543,5,3,73,64,42,97,63,76,63,8,73,97,23,45,56,89,45,3,23,2,5,78,23,56,67,78,8,3,78,34,67,23,324,234,43,544,54,33,223,443,444,234,76,432,233,23,232,243,222,221,254,222,276,300,353,354,387,364,309]
        num_bins = 6
        n, bins, patches = plt.hist(x, num_bins, facecolor = 'pink')
        plt.show()
        
    def req(self):
        # Search GitHub's repositories for requests
        response = requests.get(
             'https://api.github.com/search/repositories',
             params={'q': 'requests+language:python'},
        )

        # Inspect some attributes of the `requests` repository
        json_response = response.json()
        repository = json_response['items'][0]
        print(f'Repository name: {repository["name"]}')  # Python 3.6+
        print(f'Repository description: {repository["description"]}')  # Python 3.6+

    def req1(self):
        response = requests.get(
            'https://api.github.com/search/repositories',
             params={'q': 'requests+language:python'},
             headers={'Accept': 'application/vnd.github.v3.text-match+json'},
        )

        # View the new `text-matches` array which provides information
        # about your search term within the results
        json_response = response.json()
        repository = json_response['items'][0]
        print(f'Text matches: {repository["text_matches"]}')


    def req2(self):
        x = requests.get('https://w3schools.com/python/demopage.htm')

        print(x.text)       


    def mt(self):
       plt.plot([1, 2, 3, 4])
       plt.ylabel('some numbers')
       plt.plot([1, 2, 3, 4],'g--d')
       plt.show()




    def panggil(self):
        self.ganjilgenap()
        self.urutan()
        self.tambah()
        self.metplot()
        self.acak()
        self.histogram()
        self.req()
        self.req1()
        self.req2()
        self.mt()

                    