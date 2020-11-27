# ficou confuso, refazer depois

entrada = int(input('wentrada: '))
cont = entrada - 1
cont2 = 0
cont3 = -1
cont4 = ((entrada - 1) * 2) - 1

print(' ' * (entrada - 1) + '#' + ' ' * (entrada - 1))

for x in range(entrada - 1):
    cont -= 1
    cont3 += 2
    print(' ' * cont + '#' + ' ' * cont3 + '#')

for x in range(entrada - 2):
    cont2 += 1
    cont4 -= 2
    print(' ' * cont2 + '#' + ' ' * cont4 + '#')

print(' ' * (entrada - 1) + '#' + ' ' * (entrada - 1))

