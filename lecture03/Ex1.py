
def f(x):
    return x ** 2


g = f

#print(type(f))
#print(type(g))

#print(f(4))
#print(g(4))


''''''

def calc1(x):
    return x*10


#print(calc1(10))


def calc2(x):
    return x*10


#print(calc2(10))


def math(op, x):
    print(op(x))


#math(calc2, 10)


''''''

def sum(x,y):
    return x+y
# Этот метод можно представить проще:
sum = lambda x, y: x + y

def mult(x, y):
    return x * y


def calc(op, a, b):
    print(op(a,b))
    # return op(a, b)


#calc(mult, 4, 5)
# ее можно переписать вот так:
#calc(lambda x, y: x + y, 4, 5)


''''''


lst = []
for i in range(1, 101):
    if(i % 2 == 0):
        lst.append(i)

#print(lst)

lst = [i for i in range(1, 11) if(i % 2 == 0)]
print(lst)

def f(x):
    return x ** 3

# последовательность: for, if, f(i)
lst1 = [f(i) for i in range(1, 11) if(i % 2 == 0)]
#print(lst1)

lst2 = [(i, f(i)) for i in range(1, 11) if(i % 2 == 0)]
#print(lst2)


''''''

