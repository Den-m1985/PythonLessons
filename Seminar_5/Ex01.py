lst = [1, 2, 3, 5, 6, 9, 78, -665]


# f1 = lambda x: x*x это выражение некорректное, при форматитровании выдает следущее:
def f1(x): return x*x


print(max(map(abs, lst)))  # возврашает максимальное число по модулю (abs).
print(max(lst, key=abs))  # возврашает максимальное число (abs).


lst2 = [(1, 8), (6, 2), (4, 2), (6, 1)]  # список из кортежей
# возврашает максимальное число по индексу [1].
print(max(lst2, key=lambda x: x[1]))


#a, b, c = map(int, input().split())
#print(a, b, c)

#item = list(map(int, input().split()))
# print(item)

a = int('1011', 2)  # число в двоичной системе счисл.
print(a)  # выводит в 10тичной


lst3 = [2, 3, 6, 5, 8, 9, 7, 2, 3]
a = filter(lambda x: x % 2 == 0, lst3)
print(*a)  # *a выводит без скобок, а значит это не список.
