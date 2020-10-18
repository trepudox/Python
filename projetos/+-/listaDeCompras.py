listacompras = []

while True:
    try:
        produto = input('Nome do produto: ')
        quantia = int(input('Quantidade: '))
        preco = float(input('Preço unitário: '))
    except ValueError:
        print('\nDigite dados válidos por favor.\n')
        continue

    listacompras.append((produto, quantia, preco))

    condic = input('\nDigite "S" para continuar e "P" para parar.\n')

    if condic.casefold() == "s":
        continue
    else:
        print()
        break

for x in listacompras:
    print("Produto:          {}\nQuantidade:       {}\nPreço unitário:   {:.2f}\nPreço total:      {:.2f}".format(x[0], x[1], x[2], x[1]*x[2]))
    print()

print('Fim do programa.')
