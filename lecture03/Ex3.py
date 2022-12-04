li = [x for x in range(1, 20)]

li = list(map(lambda x: x + 10, li))

print(li)

# получаем список с терминала
#data = list(map(int, input().split()))
#print(data)


''''''

# Фильтруем данные
data2 = [x for x in range(10)]
res = list(filter(lambda x: not x % 2, data2))
print(res)
