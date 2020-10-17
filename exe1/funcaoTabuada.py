def tabuada10(x):
    lista = list(range(11))
    for i in range(0,11):
        lista[i] = x * i

    return lista

print(tabuada10())