lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [0, 5, 1, 4]

resultado = []

for index, i in enumerate(lista2):
    resultado.append(i + lista1[index])

print(resultado)