def pulalinha():
    print()


class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False
        self._sembateria = False

    def ligar(self):
        if self._ligado:
            print(f'{self._nome} já está ligado.')
        else:
            self._ligado = True
            print(f'{self._nome} agora está ligado.')

        pulalinha()

    def desligar(self):
        if self._ligado:
            self._ligado = False
            print(f'{self._nome} agora está desligado.')
        else:
            print(f'{self._nome} já está desligado.')

        pulalinha()

    def tem_bateria(self):
        if self._sembateria:
            print(self._nome, 'está sem bateria.')
        else:
            print(self._nome, 'ainda tem bateria.')

        pulalinha()

    def acabar_bateria(self):
        self._sembateria = True
        print(self._nome, 'está sem bateria...')
        self.desligar()

        pulalinha()

    def carregar_bateria(self):
        self._sembateria = False
        print(self._nome, 'agora está com a bateria carregada.')

        pulalinha()


class Celular(Eletronico):
    def __init__(self, modelo, marca, cor, armazenamento):
        super().__init__(modelo)
        self._marca = marca
        self._cor = cor
        self._armazenamento = armazenamento

    def fazer_ligacao(self):
        print(self._nome, 'está fazendo uma ligação.')

        pulalinha()


if __name__ == '__main__':
    ele1 = Eletronico('Celular')

    ele1.ligar()
    ele1.desligar()
    ele1.tem_bateria()
    ele1.ligar()
    ele1.acabar_bateria()

    cel1 = Celular('J8', 'Samsung', 'Preto', 64)

    cel1.fazer_ligacao()
