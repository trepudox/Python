minutos = int(input('Digite os minutos que você passou este mês no telefone: '))

if minutos < 200:
    preco = 0.20
elif 200 <= minutos < 400:
    preco = 0.18
elif minutos >= 400:
    preco = 0.15

total = preco * minutos
print('O valor total será de {:.2f} reais, levando em consideração os {} que você passou no telefone este mês.'.format(total, minutos))