class Gato:
    def __init__(self, cor, tamanho, nome='Gato'):
        self.cor = cor
        self.tamanho = tamanho
        self.nome = nome
        self.comendo = False
        self.bebendo = False
        self.ronronando = False

    def miar(self):
        if self.comendo:
            print(self.nome + ' tentou miar comendo kkkk muito burro.')
        else:
            print(self.nome + ' miou. Miau!')

    def comer(self):
        if self.bebendo:
            print(self.nome + ' está bebendo água e não pode comer agora.')
        else:
            print(self.nome + ' agora está comendo.')
        self.comendo = True

    def beber(self):
        if self.comendo:
            print(self.nome + ' está comendo e não pode beber água agora.')
        else:
            print(self.nome + ' agora está bebendo água.')
            self.bebendo = True

        if self.ronronando:
            print('vrum')

    def parar(self):
        lista_acoes = [self.comendo, self.bebendo]
        if any(lista_acoes):
            self.comendo = False
            self.bebendo = False
            if self.ronronando:
                print('vrum')
            print(self.nome + ' agora está livre para fazer o que quiser.')
        else:
            if self.ronronando:
                print('vrum')
            print(self.nome + ' já não estava fazendo nada, gato vagabundo.')

    def parar_ronronar(self):
        if self.ronronando:
            self.ronronando = False
            print('vrum')
            print(self.nome + ' parou de ronronar.')
        else:
            print(self.nome + ' não estava ronronando.')

    def ronronar(self):
        if self.ronronando:
            print('vrum')
            print(self.nome + ' já estava ronronando.')
        else:
            self.ronronando = True
            print('vrum')
            print(self.nome + ' agora está ronronando.')


if __name__ == '__main__':
    gato1 = Gato('preto', 'pequeno', 'Jaspion')

    gato1.miar()

    gato1.comer()

    gato1.miar()

    gato1.parar()

    gato1.beber()

    print('\nFim do programa.')
