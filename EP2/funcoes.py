from random import randint
def rolar_dados (n):
    l = []
    for k in range (0, n, 1):
        a = randint(1, 6)
        l.append(a)
    return l


