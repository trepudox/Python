listaNum = list(range(1, 101))
listaNumPares = [i for i in listaNum if i % 2 == 0]
listaNumImpares = []

print(listaNum)
print(listaNumPares)

listaNumImpares = list(map(lambda x: x - 1, listaNumPares))
print(listaNumImpares)
