import emoji

# pip install emoji
# tic tac toe game
# 1. Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP
# :skull:
# :Christmas_tree:
# :Santa_Claus:
# :alien:
# https://carpedm20.github.io/emoji/    берем emoji от сюда

print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

base_emoji = emoji.emojize(':skull:')
smile_first_player = emoji.emojize(':Christmas_tree:')
smile_second_player = emoji.emojize(':Santa_Claus:')
square = {i: base_emoji for i in range(1, 10)}


# рисует игровое поле
def draw_board(square):
    for row in range(1, 9, 3):
        print('  '.join(square[key] for key in range(row, row + 3)))


# принимает ввод пользователя. Проверяет корректность ввода
def take_input(smile):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + smile+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if square[player_answer] in base_emoji:
                square[player_answer] = smile
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


# функция проверки игрового поля, проверяет, выиграл ли игрок
def check_win(square):
    #  проверка по строкам
    if square[1] == square[2] and square[2] == square[3]:
        return square[1]
    elif square[4] == square[5] and square[5] == square[6]:
        return square[4]
    elif square[7] == square[8] and square[8] == square[9]:
        return square[7]
    #  проверка по столбам
    elif square[1] == square[4] and square[4] == square[7]:
        return square[1]
    elif square[2] == square[5] and square[5] == square[8]:
        return square[2]
    elif square[3] == square[6] and square[6] == square[9]:
        return square[3]
    #  проверка по диагонали
    elif square[1] == square[5] and square[5] == square[9]:
        return square[1]
    elif square[3] == square[5] and square[5] == square[7]:
        return square[3]
    return False


# функция запускает и управляет игровым процессом.
def main(square):
    count = 0
    win = False
    while not win:
        draw_board(square)
        if count % 2 == 0:
            take_input(smile_first_player)
        else:
            take_input(smile_second_player)
        count += 1
        if count > 4:
            tmp = check_win(square)
            if tmp:
                print()
                print(tmp, "выиграл!\n")
                win = True
                break
        if count == 9:
            print()
            print("Ничья!\n")
            break
    draw_board(square)


main(square)

input("Нажмите Enter для выхода!")
