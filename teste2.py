def dec1(func):
    def a(texto):
        print('-' * (len(texto) + 2))
        func(' ' + texto + ' ')
        print('-' * (len(texto) + 2))
    return a


@dec1
def comandos(*args):
    return 'aaa'


comandos()
