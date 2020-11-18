from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade


class Aluno(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)


p1 = Aluno('marco', 18)
