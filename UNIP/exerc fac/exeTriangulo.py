l1 = input('Digite um número: ')
l2 = input('Digite outro número: ')
l3 = input('Digite outro número: ')

if (l1 and l2 and l3).isnumeric():
    l1 = int(l1)
    l2 = int(l2)
    l3 = int(l3)
else:
    print('Por favor digite valores válidos.')

if (type(l1) and type(l2) and type(l3)) == int:
    if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
        if l1 == l2 and l3:
            print('Triângulo Equilátero.')
        elif l1 == l2 or l1 == l3 or l2 == l3:
            print('Triângulo Isósceles.')
        else:
            print('Triângulo Escaleno.')
    else:
        print('Por favor digite valores válidos')
