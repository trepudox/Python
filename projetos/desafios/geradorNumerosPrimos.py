import random


def e_primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True


entrada = int(input('Digite o tamanho desejado do número: '))
if entrada < 1:
    raise ValueError('Valor não pode ser menor ou igual a 0')

while True:
    numero = str(random.randint(1, 9))
    for x in range(entrada - 1):
        numero += str(random.randint(0, 9))

    numero = int(numero)

    if e_primo(numero):
        print(f'O número {numero} é primo.')
        break
