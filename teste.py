lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [0, 5, 1, 4]

resultado = [a+b for a, b in zip(lista1, lista2)]

print(resultado)
