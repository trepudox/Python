contador = 0
pessoas = int(input('Número de pessoas: '))
idade = 0
media = 0

while contador < pessoas:
    idade = int(input('Coloque a idade: '))
    media += idade
    contador += 1
else:
    resultado = media / pessoas
    print('A média de idades é: {:.2f}'.format(resultado))
