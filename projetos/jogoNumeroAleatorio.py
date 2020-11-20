from random import randint

vidas = 10
numero_aleatorio = randint(0, 100)
print('Você tem que adivinhar um número aleatório entre 0 e 100, você tem 10 chances.')
while vidas > 0:
    try:
        entrada = int(input('\nDigite um número de 0 a 100: '))
        if entrada < 0 or entrada > 100:
            raise ValueError
    except ValueError:
        print('\nValor tem que ser um número inteiro de 0 a 100.')
        continue

    if entrada == numero_aleatorio:
        print('\nVocê ganhou!')
        print(f'O número era {numero_aleatorio} e você ainda tinha {vidas} vidas.')
        break

    if entrada > numero_aleatorio:
        print(f'Muito alto! O número é menor que {entrada}.')
        vidas -= 1
        print(f'Você ainda tem {vidas} vidas.')
        continue

    if entrada < numero_aleatorio:
        print(f'Muito baixo... O número é maior que {entrada}.')
        vidas -= 1
        print(f'Você ainda tem {vidas} vidas.')
else:
    print(f'Você perdeu, suas vidas chegaram a 0.\nO número aleatório era {numero_aleatorio}.')

print('\nFim do jogo.')
