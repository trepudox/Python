def quadrado(lista):
    for x in lista:
        yield x*x


for valor in quadrado(list(range(10))):
    print(valor)
