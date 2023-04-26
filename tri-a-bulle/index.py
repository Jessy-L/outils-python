import math as math
import random 

tab = []

def tabalea():
    for _ in range(10):
        tab.append(random.randint(0,10000))
    return tab

tabalea()


def tri():
    n  = len(tab)
    for i in range(n):

        for j in range(0, n - i - 1):
            if tab[j + 1] < tab[j]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
    return tab

print(tri())