from abc import ABC, abstractmethod


def pulalinha():
    print()


class Animal(ABC):
    @abstractmethod
    def __init__(self, patas: int, olhos: int):
        self._patas = patas
        self._olhos = olhos
        self._dormindo = False
        self._comendo = False
        self._bebendo = False
        self._morto = False

    def dormir(self):
        if self._morto:
            print('A ação não pode ser feita,', self._nome, 'está morto.')
            pulalinha()
            return

        if self._dormindo:
            print(self._nome, 'já está dormindo.')
            pulalinha()
            return

        if self._comendo:
            print(self._nome, 'parou de comer e foi dormir.')
            self._comendo = False

        if self._bebendo:
            print(self._nome, 'parou de beber e foi dormir.')
            self._bebendo = False

        self._dormindo = True
        print(self._nome, 'agora está dormindo.')
        pulalinha()

    def comer(self):
        if self._morto:
            print('A ação não pode ser feita,', self._nome, 'está morto.')
            pulalinha()
            return

        if self._dormindo:
            print(self._nome, 'não pode comer dormindo.')
            pulalinha()
            return

        if self._bebendo:
            print(self._nome, 'não pode comer enquanto bebe.')
            pulalinha()
            return

        self._comendo = True
        print(self._nome, 'agora está comendo.')
        pulalinha()

    def beber(self):
        if self._morto:
            pulalinha()
            print('A ação não pode ser feita,', self._nome, 'está morto.')
            return

        if self._dormindo:
            print(self._nome, 'não pode beber dormindo.')
            pulalinha()
            return

        if self._comendo:
            print(self._nome, 'não pode beber enquanto come.')
            pulalinha()
            return

        self._bebendo = True
        print(self._nome, 'agora está comendo.')
        pulalinha()

    def parar(self):
        if self._morto:
            print('A ação não pode ser feita,', self._nome, 'está morto.')
            pulalinha()
            return

        if self._dormindo:
            print(self._nome, 'agora está acordado.')
            self._dormindo = False
            pulalinha()
            return

        if self._comendo:
            print(self._nome, 'parou de comer.')
            self._comendo = False
            pulalinha()
            return

        if self._bebendo:
            print(self._nome, 'parou de beber')
            self._bebendo = False
            pulalinha()
            return


class Cachorro(Animal):
    def __init__(self, nome: str, raca: str, porte: str, idade: int, _patas=4, _olhos=2):
        super().__init__(_patas, _olhos)
        self._nome = nome
        self._raca = raca
        self._porte = porte
        self._idade = idade
        self._vidas = 3

    def latir(self):
        if self._morto:
            print(self._nome, 'está morto.')
            pulalinha()
            return
        print(self._nome, 'latiu.')
        pulalinha()

    def atacar(self, other):
        if self._morto and other._morto:
            print('A ação não pode ser feita,', self._nome, 'e', other._nome, 'estão mortos.')
            pulalinha()
            return

        elif self._morto:
            print('A ação não pode ser feita,', self._nome, 'está morto.')
            pulalinha()
            return

        elif other._morto:
            print('A ação não pode ser feita,', other._nome, 'está morto.')
            pulalinha()
            return

        print(self._nome, f'atacou {other._nome}!')
        other._vidas -= 1
        if other._vidas >= 1:
            print(other._nome, f'agora tem {other._vidas} vidas.')
            pulalinha()
        else:
            print(other._nome, 'está sem vidas, portanto, morreu...')
            pulalinha()
            other._morto = True


if __name__ == '__main__':
    cao1 = Cachorro('Rex', 'Labrador', 'Médio', 3)
    cao1.comer()
    cao1.beber()
    cao1.parar()
    cao1.beber()
    cao1.dormir()
    cao1.latir()
    cao2 = Cachorro('Tarzan', 'Vira-Lata', 'Médio', 5)
    cao2.atacar(cao1)
    cao2.atacar(cao1)
    cao2.atacar(cao1)
