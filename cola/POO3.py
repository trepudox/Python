from abc import ABC, abstractmethod


def pula_linha():
    print()


class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @abstractmethod
    def dados(self):
        print('Nome:', self._nome)
        print('Idade:', self._idade)


class Paciente(Pessoa):
    def __init__(self, nome, idade, id):
        super().__init__(nome, idade)
        self._id = id
        self._estado = 'Normal'
        self._internado = False
        self._morto = False

    def dados(self):
        super().dados()
        try:
            print('Tipo sanguíneo:', self.sangue.tipo)
        except AttributeError:
            print('Tipo sanguíneo:', 'Ainda não registrado')
        if self._morto:
            print('Infelizmente morreu...')
            pula_linha()
            return
        print('Internado:', self._internado)
        pula_linha()

    def morrer(self):
        print(self._nome, 'morreu...')
        self._morto = True
        pula_linha()

    def internar(self):
        print(self._nome, 'está internado agora em estado', self._estado)
        self._internado = True
        pula_linha()


class Sangue:
    def __init__(self, tipo: str):
        self.tipo = tipo.upper()

    def tipo_sanguineo(self):
        print('O tipo sanguíneo é', self.tipo)
        pula_linha()


if __name__ == '__main__':
    paciente1 = Paciente('Marco', 18, 1)

    paciente1.dados()

    paciente1.sangue = Sangue('o-')

    paciente1.sangue.tipo_sanguineo()

    paciente1.dados()

    paciente1.morrer()

    paciente1.dados()
