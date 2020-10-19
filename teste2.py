import time


def quadrado(nums):
    res = []
    for x in nums:
        res.append(x*x)
        time.sleep(0.5)

    return res


lista = []
for elemento in quadrado(list(range(10))):
    print(elemento)
    lista.append(elemento)
    print(lista)