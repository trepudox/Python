def dec1(func):
    def dec(texto):
        print('-' * (len(texto) + 2))
        func(' ' + texto + ' ')
        print('-' * (len(texto) + 2))

    return dec


@dec1
def printar(texto):
    print(texto)


printar('aaaaa')
print()
printar('aaaaa')
