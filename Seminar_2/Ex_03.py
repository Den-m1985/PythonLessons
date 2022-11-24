'''
 Напишите программу, в которой пользователь будет задавать две строки, 
   а программа - определять количество вхождений одной строки в другой.

s1 = 'aa ab aba ewfwef'
s2 = 'aba'

print(s1.count(s2))
'''


some_str_1 = 'aaababaewfwef'
some_str_2 = 'aba'
len_str_2 = len(some_str_2)
i = 0
count = 0
while i + len_str_2 < len(some_str_1):
    if some_str_1[i:i + len_str_2] == some_str_2:
        count += 1
    i += 1
print(count)
