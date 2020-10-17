distancia = int(input('Digite arredondadamente a distância em quilômetros que você percorrerá na viagem: '))
preco = 0
if distancia <= 200:
    print('Você pagará R$ ' + str(distancia * 0.5))
elif distancia > 200:
    print('Você pagará R$ ' + str(distancia * 0.45))