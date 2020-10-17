import random

cartas = {'Dois': 2, 'Três': 3, 'Quatro': 4, 'Cinco': 5, 'Seis': 6, 'Sete': 7, 'Oito': 8, 'Nove': 9, 'Dez': 10,
          'Valete': 10, 'Dama': 10, 'Rei': 10, 'Ás': 11}
cartas_lista = ['Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Valete', 'Dama', 'Rei', 'Ás']

lista = list(range(0, 12))
aleatorio = lista[random.choice(lista)]
pontos = 0

pontos += cartas.get(cartas_lista[aleatorio])

print('Você tirou a carta {}, você agora possui {} pontos.'.format(cartas.get(cartas_lista[aleatorio]), pontos))
