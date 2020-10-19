def exemplo(listaarg):
    for i in listaarg:
        yield i * i


var = exemplo(list(range(10)))
for valor in var:
    print(valor)
