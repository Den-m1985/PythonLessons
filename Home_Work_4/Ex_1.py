'''
Вычислить число Пи c заданной точностью d
Пример:
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
'''


def calculate_Pi(k):
    pi = 0
    for k in range(1, 10000):
        pi = pi+4*((-1)**(k+1))/(2*k-1)
    print(round(pi, 4))
    

calculate_Pi(1)
