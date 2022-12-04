'''
в файле хранятся числа, нужно выбрать четные числа и
составить список пар (число; квадрат числа).
пример:
1 2 3 5 8 15 23 38
Получить:
[(2,4), (8,64), (38,1444)]
'''


path = 'task.txt'
f = open(path, 'r')
data = f.read() + ' ' # Добавляем пробел
f.close()

numbers = []

while data != '':  # пробегаемся пока наша строка не пустая
    space_pos = data.index(' ')  # найти первую позицию пробела
    numbers.append(int(data[:space_pos])) #  взять все, что от первого символа до позиции первого пробела,  превратить это в число
    data = data[space_pos + 1:] # обновляем наш список

out = []
for e in numbers:
    if not e % 2:
        out.append((e, e ** 2))
#print(out)


# упрощаем задачу


def select(f,col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


data = '1 2 3 5 8 15 23 38'.split()

res = select(int, data)
print (res)
res = where(lambda x: not x % 2, res)
print(res)
res = select(lambda x: (x, x**2), res)
print(res)


# упрощаем задачу


def where(f, col):
    return [x for x in col if f(x)]


data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)
res = where(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)


# упрощаем задачу


data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)
res = filter(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)