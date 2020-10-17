hora = input('Digite que horas são: ')

if hora.isnumeric():
    hora = int(hora)
    if 0 <= hora <= 11:
        print('Bom dia!')
    elif 12 <= hora <= 17:
        print('Boa tarde!')
    elif 18 <= hora <= 23:
        print('Boa noite!')
    elif hora >= 24:
        print('Digite um valor válido por favor.')
else:
    print('Digite um valor válido por favor.')