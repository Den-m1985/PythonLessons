'''
Вычислить число Пи c заданной точностью d
Пример:
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
'''

from math import pi

#print(round(pi, 4))


def calculate_Pi():
    k = 1
    x = float(0)
    for k in range(1, 1000000):
        x = float(x)+4*((-1)**(k+1))/(2*k-1)
        #if result == round(pi, 4):
        return x

k = 1
x = 0
for k in range(1, 1000000):
    x = x+4*((-1)**(k+1))/(2*k-1)
print(x)


print(calculate_Pi())
