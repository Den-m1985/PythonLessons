import csv
import json


def csv_to_data(file_name='phonebook.csv'):
    with open(file_name, "r", newline='', encoding='utf-8') as f:
        csv_f = csv.reader(f, delimiter=';')
        data = []
        for row in csv_f:
            data.append(row)
    return data


def export_to_xml(user_file_name, data=csv_to_data()):
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<contacts>\n'
    for row in data:
        first_name, last_name, phone_number, description = row
        xml += '    <contact>\n'
        xml += '        <Name>{}</Name>\n' \
            .format(first_name)
        xml += '        <Last_name>{}</Last_name>\n' \
            .format(last_name)
        xml += '        <Phone_number>{}</Phone_number>\n' \
            .format(phone_number)
        xml += '        <Info>{}</Info>\n' \
            .format(description)
        xml += '    </contact>\n'
    xml += '</contacts>'
    with open(f'{user_file_name}.xml', 'w', encoding='utf-8') as page:

        page.write(xml)
    return data


# работает
def csv_to_json(jsonFilePath, csvFilePath='phonebook.csv'):

    jsonArray = csv_to_data()
    with open(f"{jsonFilePath}.json", 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4, ensure_ascii=False)
        jsonf.write(jsonString)
        '''
        Если sure_ascii имеет значение true (по умолчанию), 
        в выводе гарантированно будут экранированы все входящие символы, отличные от ASCII. 
        Если sure_ascii имеет значение false, эти символы будут выводиться как есть.  
        '''


''' для словарей
def export_json(user_file_name, file_name = 'phonebook.csv'):
    with open(file_name, "r", newline='', encoding='utf-8') as f:
        #csv_f = csv.reader(f, delimiter=';')
        data = []
        template = '{{"Имя": "{}", "Фамилия": "{}", "Телефон": "{}", "Описания": "{}", }}'
        
        
        fieldnames = ['Имя','Фамилия','Отчество','Дата рождения','Номер телефона','Email']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(data)
'''
