n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')

if n1.startswith('-'):
    n1 = n1.replace('-', '')
    n1 = float(n1)
    n1 = -n1
else:
    n1 = float(n1)

if n2.startswith('-'):
    n2 = n2.replace('-', '')
    n2 = float(n2)
    n2 = -n2
else:
    n2 = float(n2)

if type(n1) and type(n2) == float:
    media = (n1 + n2) / 2
    print('A média entre {:.2f} e {:.2f} é de {:.2f}'.format(n1, n2, media))
else:
    print('Por favor digite valores numéricos válidos.')
