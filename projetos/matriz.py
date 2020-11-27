entrada_linha = int(input('Quantidade de linhas da matriz: '))
entrada_coluna = int(input('Quantidade de colunas da matriz: '))
for x in range(entrada_linha):
    for y in range(entrada_coluna):
        print(f'[{x},{y}]', end=' ')
    else:
        print()
