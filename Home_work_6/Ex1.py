'''
1 предложить улучшения кода для четырёх уже решённых задач:

С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension


Начиная с 3 семинара.
'''

# 6 семинар (делали в комнате), пересдача с enumerate (строка 15)
str_ = '10+5*1-50+6'

lst = []
last = -1
for i, symbol in enumerate(str_):
    if not symbol.isdigit():
        lst.append(int(str_[last + 1:i]))
        lst.append(symbol)
        last = i
    # print(i, symbol, lst, last)

lst.append(int(str_[last + 1:i + 1]))
print(lst)

lst_1 = []
if type(lst[0]) is int:
    lst_1.append(lst[0]) 

for i, symbol in enumerate(lst):
    if symbol == "*":
        lst_1[-1] = lst_1[-1] * lst[i + 1]
    if symbol == "/":
        lst_1[-1] = lst_1[-1] / lst[i + 1]
    if symbol == "+":
        lst_1.append(lst[i + 1])
    if symbol == "-":
        lst_1.append(-lst[i + 1])

print(sum(lst_1))