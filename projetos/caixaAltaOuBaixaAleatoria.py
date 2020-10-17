import random

entrada = ''

print('Este programa vai transformar, aleatoriamente, uma letra da palavra ou frase digitada em caixa alta ou baixa. '
      'Para sair digite "!sair".')

while True:
    saida = []

    entrada = input('Digite: ')

    if entrada.casefold() == '!sair':
        break

    for indice, letra in enumerate(entrada):
        num = random.randint(0, 1)

        if indice > 0:
            if saida[indice - 1].isupper() and saida[indice - 2].isupper():
                atual = str(letra).lower()
                saida.append(atual)
                continue
            elif saida[indice - 1].islower() and saida[indice - 2].islower():
                atual = str(letra).upper()
                saida.append(atual)
                continue
            else:
                if letra.isalpha() and num == 1:
                    atual = str(letra).upper()
                    saida.append(atual)
                    continue
                elif letra.isalpha() and num == 0:
                    atual = str(letra).lower()
                    saida.append(atual)
                    continue
                else:
                    saida.append(letra)
                    continue
        else:
            if letra.isalpha() and num == 1:
                atual = str(letra).upper()
                saida.append(atual)
                continue
            elif letra.isalpha() and num == 0:
                atual = str(letra).lower()
                saida.append(atual)
                continue
            else:
                saida.append(letra)
                continue

    saida = ''.join(saida)

    print(saida + '\n')

print('\nFim do programa')
