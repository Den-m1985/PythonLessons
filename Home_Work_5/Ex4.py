'''
4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

Входные и выходные данные хранятся в отдельных текстовых файлах.

aaaasssdddwwwwwwwwwwwweeeffffff -> 4a3s3d9w3w3e6f
4a3s3d9w3w3e6f-> aaaasssdddwwwwwwwwwwwweeeffffff
'''


def read_file(file):
    with open(file, 'r') as data:
        return data.read()


def write_to_file(file_name, result):
    with open(file_name, 'w') as f_obj:
        f_obj.write(result)


def encode_rle(text):

    str_rle = ''
    temp = ''
    count = 1
    for simbol in text:
        if simbol != temp:
            if temp:  # если здесь что-то есть
                str_rle += str(count) + temp 
            count = 1
            temp = simbol
        elif count == 8:
            str_rle += str(count+1) + temp
            count = 1
            temp = ''
        else:
            count += 1
    
    str_rle += str(count) + temp
    return str_rle


def decoding_rle(text):
    count = ''
    str_decode = ''
    for char in text:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode


text = read_file('Wome_work_5_4.txt')
print(text)
str_code = encode_rle(text)
write_to_file('Wome_work_5_4(2).txt', str_code)
print(str_code)

coding_text = read_file('Wome_work_5_4(2).txt')
str_decode = decoding_rle(coding_text)
print(str_decode)
