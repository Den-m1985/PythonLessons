'''
2 Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета.
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все
конфеты у своего конкурента?

a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом"
'''
from random import randint

# Сколько конфет нужно взять первому игроку, чтобы забрать все
count_candies = 2021
max_candy = 28
count = count_candies // max_candy  # Кол-во целых делений
residue = count_candies - (count * max_candy)   # Остаток от целого деления
print(f'Что бы всегда побеждать тебе нужно ходить первым с 1 по {residue -1} конфет')
print(f'При этом тебе нужно добавлять до {max_candy} конфет')
print(f'В конце останется от 1 до 4 конфета и ты заберешь все')



'''
#Играют 2 игрока
print('Что бы выйти нажмите Enter')


def play_game(count_candies, max_candy, first_piayer):

    players = first_piayer
    while count_candies > 0:
        if players % 2 == 1:
            move = int(input(f'Ходит User2. Не более {max_candy} конфет: '))
            if move > 28 or move < 1:
                print(f'Не более {max_candy} конфет!!!!!!!!!!!!!!!!!!')
                attempt = 3
                while attempt > 0:
                    if move <= 28 and move >= 1:
                        break
                    print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'Game over!')
        else:
            move = int(input(f'Ходит User1. Не более {max_candy} конфет: '))
            if move > 28 or move < 1:
                print(f'Не более {max_candy} конфет!!!!!!!!!!!!!!!!!!')
                attempt = 3
                while attempt > 0:
                    if move <= 28 and move >= 1:
                        break
                    print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'Game over!')     
        count_candies = count_candies - move
        print(f'Осталось {count_candies} конфет')
        players += 1
        if count_candies <= max_candy:
            print('Все конфеты разобраны.')
            break
    return players % 2


count_candies = 285 #Кол-во конфет
max_candy = 28 #Кол-во конфет за ход
player1 = 'User1'
player2 = 'User2'
first_piayer = randint(1, 2)
if first_piayer == 1:
    print(f'Первый ходит {player2}')
else:
    print(f'Первый ходит {player1}')


winer = play_game(count_candies, max_candy, first_piayer)
if winer == 1:
    print(
        f'Поздравляю! В этот раз победил {player2}! Ему достаются все {count_candies} конфет!')
else:
    print(
        f'Поздравляю! В этот раз победил {player1}! Ему достаются все {count_candies} конфет!')
'''


'''
#Игра с Питоном
print('Что бы выйти нажмите Enter')


def play_game(count_candies, max_candy, first_piayer):

    players = first_piayer
    while count_candies > 0:
        if players % 2 == 1:
            move = randint(1, max_candy)
            print(f'Я забираю {move}')
        else:
            move = int(input('Твой ход. Не более 28 конфет: '))
            if move > 28 or move < 1:
                print(f'Не более 28 конфет!!!!!!!!!!!!!!!!!!')
                attempt = 3
                while attempt > 0:
                    if move <= 28 and move >= 1:
                        break
                    print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'Game over!')     
        count_candies = count_candies - move
        print(f'Осталось {count_candies} конфет')
        players += 1
        if count_candies <= max_candy:
            print('Все конфеты разобраны.')
            break
    return players % 2


count_candies = 100 #Кол-во конфет
max_candy = 28 #Кол-во конфет за ход
player1 = 'User'
player2 = 'Питон'
first_piayer = randint(1, 2)
if first_piayer == 1:
    print(f'Первый ходит {player2}')
else:
    print(f'Первый ходит {player1}')


winer = play_game(count_candies, max_candy, first_piayer)
#print(winer)
if winer == 0:
    print(
        f'Поздравляю! В этот раз победил {player1}! Ему достаются все {count_candies} конфет!')
else:
    print(
        f'Поздравляю! В этот раз победил {player2}! Ему достаются все {count_candies} конфет!')
'''



CANDIES = 60
MAX_STEP = 28
 
human = True
cur_candies = CANDIES
 
 
def get_ai_step():
    return randint(1, min(MAX_STEP, cur_candies))
 
 
def get_human_step():
    while True:
        cnt = input('Введите количество конфет: ')
        if cnt.isdigit() and 1 <= int(cnt) <= min(MAX_STEP, cur_candies):
            return int(cnt)
        print('Введено некорректное значение')
 
 
while cur_candies:
    if human:
        cnt = get_human_step()
        cur_candies -= cnt
        print(f'Пользователь взял {cnt} конфет. Осталось {cur_candies}.')
    else:
        cnt =get_ai_step()
        cur_candies -= cnt
        print(f'Бот взял {cnt} конфет. Осталось {cur_candies}.')
    human = not human
 
if human:
    print('Победил БОТ')
else:
    print('Победил человек')