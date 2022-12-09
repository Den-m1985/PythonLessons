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
    
    str_code = ''
    prev_char = ''
    count = 1
    if not text:
        return ''
    for simbol in text:
        if simbol != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = simbol
        else:
            count += 1
    else:
        str_code += str(count) + prev_char
        return str_code


def rle_encode(text):
    result = []
    text += '\0'  # dummy
    last = text[0]
    count = 1
    for char in text[1:]:
        if char != last:
            result.append(last if count == 1 else str(count)+last)
            last = char
            count = 0
        count += 1
    return ''.join(result)


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
str_code = encode_rle(text)
write_to_file('Wome_work_5_4(2).txt', str_code)
print(str_code)

coding_text = read_file('Wome_work_5_4(2).txt')
#str_decode = decoding_rle(coding_text)
#print(str_decode)
