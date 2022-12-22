import emoji

# pip install emoji
# tic tac toe game
# 1. Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP


print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)
#:skull:
#:Christmas_tree:
#:Santa_Claus:
# :alien:
# https://carpedm20.github.io/emoji/    берем emoji от сюда

square = {'1': emoji.emojize(':skull:'), '2': emoji.emojize(':skull:'), '3': emoji.emojize(':skull:\n'),
        '4': emoji.emojize(':skull:'), '5': emoji.emojize(':skull:'), '6': emoji.emojize(':skull:\n'), 
        '7': emoji.emojize(':skull:'), '8': emoji.emojize(':skull:'), '9': emoji.emojize(':skull:\n')}
square_copy = dict.copy(square) # копия словаря
square_copy ['1'] = emoji.emojize(':alien:')
for key, value in square_copy.items():
    
    print(value, end='')
print(emoji.emojize(':Santa_Claus:'))

# рисует игровое поле
def draw_board(square):
    #print("-" * 13)
    #for i in range(3):
    #    print("|", square[0+i*3], "|", square[1+i*3], "|", square[2+i*3], "|")
    #    print("-" * 13)
        for key, value in square.items():
            print(value, end='')


# принимает ввод пользователя. Проверяет корректность ввода
def take_input(player_step):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_step+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            #if (str(square[player_answer-1]) not in "XO"):
            if (str(square[player_answer-1]) not in "XO"):  # здесь переделать условие в словаре
                #square[player_answer-1] = player_step
                square[player_answer-1] = player_step   # здесь переделать замену в словаре на х
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


# функция проверки игрового поля, проверяет, выиграл ли игрок
def check_win(square):
    win_line = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),    # здесь проставить ключи словаря
                (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_line:
        if square[each[0]] == square[each[1]] == square[each[2]]:
            return square[each[0]]
    return False


# функция запускает и управляет игровым процессом.
def main(square):
    count = 0
    win = False
    while not win:
        draw_board(square)  # работат
        if count % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        count += 1
        if count > 4:
            tmp = check_win(square)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if count == 9:
            print("Ничья!")
            break
    draw_board(square)


#main(square)

input("Нажмите Enter для выхода!")

'''
print(emoji.emojize(':thumbs_up:'))
desc = {1: emoji.emojize(':thumbs_up:'), "2": emoji.emojize(':thumbs_up:'), 
        "3": emoji.emojize(':thumbs_up:\n'), "4": emoji.emojize(':thumbs_up:'), 
        "5": emoji.emojize(':thumbs_up:'), "6": emoji.emojize(':thumbs_up:\n'), 
        "7": emoji.emojize(':thumbs_up:'), "8": emoji.emojize(':thumbs_up:'), 
        "9": emoji.emojize(':thumbs_up:')}

for key, value in desc.items():
    print(value, end='')
'''
