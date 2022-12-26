import csv
import os
os.chdir(os.path.dirname(__file__))


# этот метод используется для добавления контакта
def write_csv(data):
    for i in range(len(data)):
        with open('phonebook.csv', "a", encoding='utf-8') as fil:
            csv_fil = csv.writer(fil, delimiter=';')
            csv_fil.writerow(data[i])


# Читаем csv для п.2
def read_contact(unit = 1, file_name = 'phonebook.csv'):
    data =''
    with open(file_name, "r", newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            data += ' '.join(row)
           
    return data
#print(read_contact())