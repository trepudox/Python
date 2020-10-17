listacompras = []

while True:
    try:
        produto = input('Nome do produto: ')
        quantia = int(input('Quantidade: '))
        preco = float(input('Pre�o unit�rio: '))
    except ValueError:
        print('\nDigite dados v�lidos por favor.\n')
        continue

    listacompras.append([produto, quantia, preco])

    condic = input('\nDigite "S" para continuar e "P" para parar.\n')

    if condic.casefold() == "s":
        continue
    else:
        print()
        break

for x in listacompras:
    print("Produto:          {}\nQuantidade:       {}\nPre�o unit�rio:   {:.2f}\nPre�o total:      {:.2f}".format(x[0], x[1], x[2], x[1]*x[2]))
    print()

print('Fim do programa.')