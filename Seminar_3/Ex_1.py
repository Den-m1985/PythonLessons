import datetime

'''
1. Реализуйте алгоритм задания случайных чисел без использования встроенного 
   генератора псевдослучайных чисел.
'''


def time1():
    return (datetime.datetime.now().microsecond // 100 % 10) **\
        (datetime.datetime.now().microsecond % 10)


print(time1())
