def e_primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True


entrada = int(input('Digite um número: '))
condic = 'é' if e_primo(entrada) else 'não é'
print('O número {} {} primo.'.format(entrada, condic))

