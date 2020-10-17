lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


# o primeiro numero que se repetir dentro das listas será retornado, caso nenhum se repita, retornará None


def funcao_repetido(lista_arg):
    lista_bau = [99 for i in range(10)]

    if len(set(lista_arg)) == len(lista_arg):
        return None

    for indice, elemento in enumerate(lista_arg):

        for indice_for2, elemento_for2 in enumerate(lista_arg[indice + 1:]):
            if elemento == elemento_for2:
                conta = indice_for2 + indice
                lista_bau[indice] = conta
                break

    return lista_arg[lista_bau.index(min(lista_bau))]


print(funcao_repetido([1, 2, 3, 3, 2, 1]))

for numero, listas in enumerate(lista_de_listas_de_inteiros):
    print(f'Lista {numero}:', funcao_repetido(listas))
