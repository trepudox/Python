from abc import ABC, abstractmethod


def pulalinha():
    print()


class Eletronico(ABC):
    @abstractmethod
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False
        self._sembateria = False

    @abstractmethod
    def __add__(self, other):
        pass

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
    def __init__(self, modelo, marca, cor, armazenamento, memoria):
        super().__init__(modelo)
        self._marca = marca
        self._cor = cor
        self._armazenamento = armazenamento
        self._memoria = memoria

    def __add__(self, other):
        return Celular()

    def fazer_ligacao(self):
        if self._ligado:
            print(self._nome, 'está fazendo uma ligação.')
        else:
            print(self._nome, 'está desligado, impossível fazer uma ligação agora.')

        pulalinha()

    def especificacoes(self):
        print(f'Especificações {self._nome}:\n\tMarca: {self._marca}\n\tModelo: {self._nome}\n\tCor: {self._cor}\n'
              f'\tArmazenamento: {self._armazenamento} GB\n\tMemória RAM: {self._memoria} GB')

        pulalinha()


class CelularSamsung(Celular):
    def __init__(self, modelo, cor, armazenamento, memoria, marca='Samsung'):
        super().__init__(modelo, marca, cor, armazenamento, memoria)
        self._marca = 'Samsung'

    def __add__(self, other):
        return CelularSamsung(f'{self._nome} + {other._nome}', f'{self._nome} + {other._nome}', (self._armazenamento + other._armazenamento), (self._memoria + other._memoria))


if __name__ == '__main__':
    cel1 = Celular('J8', 'Samsung', 'Preto', 64, 4)
    cel1.ligar()
    cel1.fazer_ligacao()

    celSamsung1 = CelularSamsung('J8', 'Preto', 64, 4)
    celSamsung2 = CelularSamsung('J1 Mini', 'Dourado', 8, 1)

    celSamsung1.especificacoes()

    celSamsung1.ligar()

    celSamsung3 = CelularSamsung

    celSamsung3 = celSamsung1 + celSamsung2
    celSamsung3.especificacoes()
