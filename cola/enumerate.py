lista = []

while len(lista) < 10:
    lista.append(input('Digite o valor: '))

for indice, valor in enumerate(lista):

    print('[{}]'.format(indice), valor)
