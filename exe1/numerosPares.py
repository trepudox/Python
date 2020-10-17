num = input('Digite um número: ')

if num.startswith('-'):
    num = num.replace('-', '')
    if num.isnumeric():
        num = int(num)
        if num % 2 == 0:
            print('O número -{} é par'.format(num))
        else:
            print('O número -{} é ímpar'.format(num))
    else:
        print('O valor digitado é inválido.')
elif num.isnumeric():
    num = int(num)
    if num % 2 == 0:
        print('O número {} é par'.format(num))
    else:
        print('O número {} é ímpar'.format(num))
else:
    print('O valor digitado é inválido.')