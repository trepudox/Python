x = 0
y = 0
numEsc = input('Digite o número de linhas e colunas desejadas: ')

if numEsc.isnumeric():
    numEsc = int(numEsc)

    while x <= numEsc:
        y = 0
        while y <= numEsc:
            print('[{:0>2} {:0>2}]'.format(x, y), end=' ')
            y += 1
        print()
        x += 1

else:
    print('Digite um valor válido.')