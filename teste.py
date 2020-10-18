import time


def quadrado(nums):
    for x in nums:
        yield x*x
        time.sleep(0.5)


lista = []
for elemento in quadrado(list(range(10))):
    print(elemento)
    lista.append(elemento)
    print(lista)

# qualquenjskofsdiosdop