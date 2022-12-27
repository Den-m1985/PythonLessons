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
def read_contact(file_name = 'phonebook.csv'):
    data =[]
    with open(file_name, "r", newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        item = ''
        for row in reader:
            item = item + ', '.join(row)
            #print(item)
        return item
#print(read_contact())



# Поиск контакта
def searchcontact(searchname):
    data =''
    with open('phonebook.csv', "r", newline='', encoding='utf-8') as f:
        csv_f = csv.reader(f, delimiter=';')
        for line in csv_f:
            if searchname in line:
                data += ' '.join(line)
                break
    return data
#print(searchcontact('Иван'))