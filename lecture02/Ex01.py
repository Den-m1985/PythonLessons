colors = ['red', 'fljfdjnd','fdvdfsvsd']
# a открытие для добавления данных
# r открытие для чтения данных
# W открытие для записи данных
# w+, r+
'''
data = open('file.txt', 'w')
data.writelines(colors)
data.write('\nLINE 2\n')
data.write('\nLINE 3\n')
data.close   # нужно для закрытия файла, во избежании утечки памяти.
'''
'''
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print (line)
data.close()
'''

import hello

print(hello.f(1))