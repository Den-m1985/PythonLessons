'''
1 предложить улучшения кода для четырёх уже решённых задач:

С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension


Начиная с 3 семинара.
'''

# Домашняя №5 Пересдача по filter lambda

'''
1 Напишите программу, удаляющую из файла все слова, содержащие "абв".
text = 'ловатмивами абв пипви апыи'
'''


def read_file(file):
    with open(file,'r', encoding="utf8") as data:
        file_read = str(data.read())
    return file_read


def write_to_file(file_name, result):
    with open(file_name, 'w', encoding='utf-8') as f_obj:
        f_obj.write(result)


def delete_abc(text, value):
    result = " ".join(filter(lambda x: not value in x, text.split( )))
    return result


delete_word = 'абв'
read_txt = read_file('Wome_work_5_1.txt')
print(read_txt)
result = delete_abc(read_txt, delete_word)
write_to_file('Wome_work_5_1.txt', result)
print(result)