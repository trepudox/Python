arquivo = open('teste.txt', 'w+')
arquivo.close()

arquivo = open('teste.txt', 'a+')
quantidade = ''
x = 0

while True:
    if type(quantidade) == int:
        print()
        break

    try:
        quantidade = int(input('Digite quantas linhas deseja: '))
    except ValueError:
        print('\nDigite um número inteiro por favor.\n')
        continue

while x < quantidade:
    x += 1
    arquivo.write(input('Digite o texto da {}º linha: '.format(x)))
    arquivo.write('\n')

else:
    print()
    arquivo.seek(0)
    for linha, texto in enumerate(arquivo.readlines()):
        print('Linha {:0>2}: '.format(linha + 1), texto)

arquivo.close()
