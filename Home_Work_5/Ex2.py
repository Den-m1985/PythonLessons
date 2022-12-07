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

count_candies = 100
max_candy = 28
sum_candies = 0

'''
while count_candies > 0:
    if (count_candies - sum_candies) < 28:
        first_player_step =  int(input(f'Твой {i}й ход: '))
        second_player_step = randint(1, 29)
        print(f'Число Питона: {second_player_step}')
        sum_candies = first_player_step + second_player_step
        step +=1
print(f'Число Питона: {sum_candies}')
'''

def play_game(count_candies, max_candy):
    players = 1
    '''
    count = rules[2]
    if rules[0] % 10 == 1 and 9 > rules[0] > 10:
        letter = 'а'
    elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
        letter = 'ы'
    else:
        letter = ''
    '''
    while count_candies > 0:
        if players == 1:
            move = randint(1, max_candy)
            print(f'Я забираю {move}')
            players = 2
        else:
            print(f'Твой ход. Не более 28 конфет!!!!!!!: ')
            move = int(input())
            players = 1
        count_candies = count_candies - move
        if count_candies > 0:
            print(f'Осталось {count_candies} конфет')
        else:
            print('Все конфеты разобраны.')
            
    return players
  
winer = play_game(count_candies, max_candy)

if not winer:
    print('У нас нет победителя.')
else:
    print(
        f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')

'''
messages = ['Ваша очередь брать конфеты', 'возьмите конфеты',
            'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']


def introduce_players():
    player1 = input('Давайте познакомися. Как Вас зовут?\n')
    player2 = 'Робик'
    print(f'Очень приятно, меня зовут {player2}')
    return [player1, player2]


def get_rules(players):
    n = int(input('Сколько конфет будем разыгрывать?\n '))
    m = int(input('Сколько максимально будем брать конфет за один ход?\n '))
    first = int(input(
        f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
    if first != 1:
        first = 0
    return [n, m, int(first)]

print(0 % 2)
0 - 0
1 - 1
2 -0
'''
'''
def play_game(rules, players, messages):
    count = rules[2]
    if rules[0] % 10 == 1 and 9 > rules[0] > 10:
        letter = 'а'
    elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
        letter = 'ы'
    else:
        letter = ''
    while rules[0] > 0:
        if not count % 2:
            move = randint(1, rules[1])
            print(f'Я забираю {move}')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(
                    f'Это слишком много, можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}')
                attempt = 3
                while attempt > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f'Осталось {rules[0]} конфет{letter}')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[count % 2]


#print(greeting)

players = introduce_players()
rules = get_rules(players)

winer = play_game(rules, players, messages)
if not winer:
    print('У нас нет победителя.')
else:
    print(
        f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')
'''