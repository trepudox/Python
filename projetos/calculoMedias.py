quantidade = int(input('Digite a quantidade de itens: '))

lista_itens = list(range(quantidade))

soma = 0
cont = 0

for x in range(0, quantidade, 1):
    lista_itens[x] = float(input('Digite o {}º número: '.format(x+1)))
    soma += lista_itens[x]

media = soma / quantidade

print('A média foi de {}'.format(media))
