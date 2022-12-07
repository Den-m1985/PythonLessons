'''
1 Напишите программу, удаляющую из файла все слова, содержащие "абв".
'''


def read_file(file):
    with open(file, encoding="utf8") as data:
        file_read = data.readlines()
    return file_read


def write_to_file(file_name, result):
    with open(file_name, 'w') as f_obj:
        f_obj.write(str(result))


def delete_abc(text, value):
    result = " ".join(list(filter(lambda x: not value in x, text.split( ))))
    return result

delete_word = 'абв'
read_txt = read_file('Wome_work_5_1.txt')
print(read_txt)
result = delete_abc(read_txt, delete_word)
print(result)
write_to_file('Wome_work_5_1.txt', result)
print(result)

