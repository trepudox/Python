import random

print("Jogo de Blackjack! O jogador que atingir 21 pontos ou chegar mais próximo disso vence!")
jogadores = 0  # quantidade de jogadores
sair = "Sair"  # comando sair

cartas_valores = {'Dois': 2, 'Três': 3, 'Quatro': 4, 'Cinco': 5, 'Seis': 6, 'Sete': 7, 'Oito': 8, 'Nove': 9, 'Dez': 10,
                  'Valete': 10, 'Dama': 10, 'Rei': 10,
                  'Ás': 11}  # dict para indicar o valor da carta através do valor da lista
cartas_lista = ['Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Valete', 'Dama', 'Rei',
                'Ás']  # lista para indicar qual carta o jogador tirou

# laleat = list(range(0, 12)) - lista para tirar números aleatórios
# aleatorio = cartas_lista[random.choice(laleat)] - carta escolhida aleatóriamente

pontos_jog1 = 0  # pontos do jogador 1
pontos_jog2 = 0  # pontos do jogador 2 (caso haja)
num_cartas_jog1 = 0  # número de cartas do jogador 1
num_cartas_jog2 = 0  # número de cartas do jogador 2 (caso haja)
acao_jog1 = ''  # ação do jogador 1
acao_jog2 = ''  # ação do jogador 2 (caso haja)

while True:
    jogadores = input('Digite a quantidade de jogadores, 1 ou 2: ')
    if jogadores == '1' or jogadores == '2':
        jogadores = int(jogadores)
        break
    elif jogadores.casefold() == sair.casefold():
        break
    else:
        print('\nPor favor digite apenas 1 ou 2 para a quantidade de jogadores. Caso queira fechar o programa digite '
              '"Sair".')

if type(jogadores) == int:
    if jogadores == 1:
        print('\nO jogo te pedirá ordens, digite a letra "S" para pedir cartas e a letra "P" para parar. Seu objetivo é'
              'alcançar os 21 pontos, caso os ultrapasse você perde. Boa sorte!\n')
        print('Tire uma carta para começar.')
        while True:
            laleat = list(range(0, 12))
            aleatorio = cartas_lista[random.choice(laleat)]

            if acao_jog1.casefold() == "P".casefold():
                print('Você pediu para parar. Você fez {} pontos em {} cartas jogadas.'.format(pontos_jog1,
                                                                                               num_cartas_jog1))
                break
            elif pontos_jog1 == 21 and num_cartas_jog1 == 2:
                print('Blackjack! Você atingiu a pontuação máxima! 21 pontos em 2 cartas, parabéns!')
                break
            elif pontos_jog1 == 21:
                print('21! Você atingiu 21 pontos em {} cartas. Muito bem!'.format(num_cartas_jog1))
                break
            elif pontos_jog1 > 21:
                print('Você ultrapassou os 21 pontos. Que pena! Você fez {} pontos em {} cartas.'.format(pontos_jog1,
                                                                                                         num_cartas_jog1))
                break

            acao_jog1 = input('Digite "S" para pedir uma carta, ou "P" para parar: ')

            if acao_jog1.casefold() != "S".casefold() and acao_jog1.casefold() != "P".casefold():
                print('\nPor favor digite apenas "S" ou "P" para o funcionamento correto do programa.\n')
                continue
            elif acao_jog1.casefold() == "S".casefold():
                pontos_jog1 += cartas_valores.get(aleatorio)
                print('A carta tirada foi: {}. Esta carta vale {} pontos, agora você tem {} pontos.\n'.format(aleatorio,
                                                                                                              cartas_valores.get(
                                                                                                                  aleatorio),
                                                                                                              pontos_jog1))
                num_cartas_jog1 += 1

    else:
        print('\nO jogo pedirá ordens, digite a letra "S" para pedir cartas e a letra "P" para parar. O objetivo dos '
              'jogadores é alcançar os 21 pontos, caso os ultrapasse você perde. \nO jogador que possuir o número mais '
              'próximo de 21 vence. Boa sorte!\n')
        vencedor = ''
        perdedor = ''

        for vez in range(1, 20):

            if pontos_jog1 == 21 and pontos_jog2 == 20:
                vencedor = 'Jogador 1'
                perdedor = 'Jogador 2'
                break
            elif pontos_jog1 == 20 and pontos_jog2 == 21:
                vencedor = 'Jogador 2'
                perdedor = 'Jogador 1'
                break

            if (acao_jog1.casefold() != "P".casefold() and pontos_jog1 < 21) == False and (
                    acao_jog2.casefold() != "P".casefold() and pontos_jog2 < 21) == False:
                if pontos_jog1 == 21 != pontos_jog2:
                    vencedor = 'Jogador 1'
                    perdedor = 'Jogador 2'
                    break
                elif pontos_jog1 != 21 == pontos_jog2:
                    vencedor = 'Jogador 2'
                    perdedor = 'Jogador 1'
                    break
                elif pontos_jog1 == 21 == pontos_jog2:
                    vencedor = 'Nenhum!'
                    break
                elif pontos_jog1 == pontos_jog2:
                    vencedor = 'Nenhum!'
                    break
                else:
                    desempate_jog1 = 21 - pontos_jog1
                    desempate_jog2 = 21 - pontos_jog2

                    if desempate_jog1.__abs__() < desempate_jog2.__abs__():
                        vencedor = 'Jogador 1'
                        perdedor = 'Jogador 2'
                        break
                    elif desempate_jog1.__abs__() > desempate_jog2.__abs__():
                        vencedor = 'Jogador 2'
                        perdedor = 'Jogador 1'
                        break
                    else:
                        vencedor = 'Nenhum!'
                        break

            else:
                while acao_jog1.casefold() != "P".casefold() and pontos_jog1 < 21:
                    laleat = list(range(0, 12))
                    aleatorio = cartas_lista[random.choice(laleat)]

                    print('Vez do jogador 1.')
                    acao_jog1 = input('Digite "S" para pedir uma carta, ou "P" para parar: ')

                    if acao_jog1.casefold() == "S".casefold():
                        pontos_jog1 += cartas_valores.get(aleatorio)
                        print('A carta tirada foi: {}. Esta carta vale {} pontos, agora você tem {} pontos.\n'.format(
                            aleatorio, cartas_valores.get(aleatorio), pontos_jog1))
                        num_cartas_jog1 += 1
                        break

                    elif acao_jog1.casefold() == "P".casefold():
                        print('Você pediu para parar. Você fez {} pontos em {} cartas jogadas.\n'.format(pontos_jog1,
                                                                                                         num_cartas_jog1))
                        break

                    else:
                        print('\nPor favor digite apenas "S" ou "P" para o funcionamento correto do programa.\n')

                while acao_jog2.casefold() != "P".casefold() and pontos_jog2 < 21:
                    laleat = list(range(0, 12))
                    aleatorio = cartas_lista[random.choice(laleat)]

                    print('Vez do jogador 2.')
                    acao_jog2 = input('Digite "S" para pedir uma carta, ou "P" para parar: ')

                    if acao_jog2.casefold() == "S".casefold():
                        pontos_jog2 += cartas_valores.get(aleatorio)
                        print('A carta tirada foi: {}. Esta carta vale {} pontos, agora você tem {} pontos.\n'.format(
                            aleatorio, cartas_valores.get(aleatorio), pontos_jog2))
                        num_cartas_jog2 += 1
                        break

                    elif acao_jog2.casefold() == "P".casefold():
                        print('Você pediu para parar. Você fez {} pontos em {} cartas jogadas.\n'.format(pontos_jog2,
                                                                                                         num_cartas_jog2))
                        break

                    else:
                        print('\nPor favor digite apenas "S" ou "P" para o funcionamento correto do programa.\n')

        if vencedor == "Nenhum!":
            print('Empate! \nJogador 1 teve {} pontos em {} cartas. \nJogador 2 teve {} pontos em {} cartas.'.format(
                pontos_jog1, num_cartas_jog1, pontos_jog2, num_cartas_jog2))
        elif vencedor == "Jogador 1":
            print('O {} venceu! {} fez {} pontos em {} cartas. Já o {} fez {} em {} cartas.'.format(vencedor, vencedor,
                                                                                                    pontos_jog1,
                                                                                                    num_cartas_jog1,
                                                                                                    perdedor,
                                                                                                    pontos_jog2,
                                                                                                    num_cartas_jog2))
        else:
            print('O {} venceu! {} fez {} pontos em {} cartas. Já o {} fez {} em {} cartas.'.format(vencedor, vencedor,
                                                                                                    pontos_jog2,
                                                                                                    num_cartas_jog2,
                                                                                                    perdedor,
                                                                                                    pontos_jog1,
                                                                                                    num_cartas_jog1))

print('Fim do programa.')
