numero = int(input('Escolha o número que quer saber da tabuada: '))
tab = int(input('Escolha por até qual valor quer que seja multiplicado: '))

for x in range(1, tab + 1, 1):
    print('{} x {} = {}'.format(numero, x, numero*x))