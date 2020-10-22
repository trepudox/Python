from itertools import zip_longest

lista1 = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 1234]
lista2 = [0, 5, 1, 4]

resultado = [a+b for a, b in zip_longest(lista1, lista2, fillvalue=0)]

print(resultado)
