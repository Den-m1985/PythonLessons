'''
1 предложить улучшения кода для четырёх уже решённых задач:

С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension


Начиная с 3 семинара.
'''

#Семинар 5. 2. Напишите программу, удаляющую из текста все слова, содержащие "абв"
# Пересдача

text = 'ловатмивами абв пипви апыи'
result = " ".join(list(filter(lambda x: not 'абв' in x, text.split( ))))
print(result)

