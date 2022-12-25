import controller


def greeting():
    print()
    print('<<ТЕЛЕФОННЫЙ СПРАВОЧНИК>>')


def menu():
    while True:
        print('\nМЕНЮ')
        print('1. Добавить новую запись')  # Работает
        print('2. Вывод записей на экран')  # Работает
        print('3. Скопировать данные в файл?')  # надо добавить копирование в json
        print('4. Сохранить в нашу базу данных?') # надо сделать
        print('5. Поиск записи')  # работает
        print('6. Выход\n')   # работает
        number = input('Выберите пункт меню: ')
        controller.distribute(number)
        if number =='6':
            break
 

greeting()
menu()