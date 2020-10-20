dic = {'Arroz': 10.0, 'Alface': 20.0, 'Feijão': 999.0}
condicao = ''
while True:
    condicao = input('Digite o que quer fazer, "V" para ver preços, "A" para adicionar produtos, e "!sair" para sair: ')
    if condicao.casefold() == '!sair':
        break
    elif condicao.casefold() == 'v':
        entrada = input('Digite o produto desejado para saber o preço: ').title()
        print(f'{entrada} custa R$', dic.get(entrada), '\n')
    elif condicao.casefold() == 'a':
        produtoadd = str(input('Digite o nome do produto: ')).title()
        dic[produtoadd] = float(input(f'Digite o valor de "{produtoadd}": '))
        print(f'Agora o dicionário ficou assim: ')
        print(dic, '\n')

print('Fim do programa.')
