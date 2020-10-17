from random import randint


def caixa(entrada='texto'):
    if len(entrada) == 0:
        raise ValueError('Texto inválido.')

    saida = entrada[0].upper() if randint(0, 1) == 1 else entrada[0].lower()
    saida += entrada[1].upper() if randint(0, 1) == 1 else entrada[1].lower()

    for indice, letra in enumerate(entrada[2:]):
        if saida[indice].islower() and saida[indice + 1].islower():
            saida += entrada[indice+2].upper()
        elif saida[indice].isupper() and saida[indice + 1].isupper():
            saida += entrada[indice+2].lower()
        else:
            saida += entrada[indice+2].upper() if randint(0, 1) == 1 else entrada[indice+2].lower()

    return saida


print(caixa(input('Digite seu texto: ')))