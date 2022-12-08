'''
4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

Входные и выходные данные хранятся в отдельных текстовых файлах.

aaaasssdddwwwwwwwwwwwweeeffffff -> 4a3s3d9w3w3e6f
4a3s3d9w3w3e6f-> aaaasssdddwwwwwwwwwwwweeeffffff
'''

    
def read_file(file):
    with open(file,'r') as data:
        return str(data.read())
     

def write_to_file(file_name, result):
    with open(file_name, 'w') as f_obj:
        f_obj.write(result)


def encode_rle(text):
    str_code = ''
    prev_char = ''
    count = 1
    for simbol in text:
        if simbol != prev_char:
            if count <10:
                str_code += str(count) + prev_char
            else:
                str_code += str(count) + prev_char
            count = 1
            prev_char = simbol
        else:
            count += 1
    return str_code


text = read_file('Wome_work_5_3.txt')        
str_code = encode_rle(text)
print(str_code)
'''
with open('Wome_work_5_3.txt', 'r') as data:
    my_text2 = data.read()

def decoding_rle(ss:str):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char 
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode
str_decode = decoding_rle(my_text2)
print(str_decode)
'''