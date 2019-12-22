import csv
class Tadi_salah_pak_saya_kira_boleh_pake_inputan_user(object):

    def Penjumlahan_yang_terencana(self):
        with open('kelas_2b/penjumlahan.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                print(f'\t{row[0]} + {row[1]} = {row[2]}.')