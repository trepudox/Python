class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def correr(self):
        print(f'O {self.__class__.__name__}', self.nome, 'agora está correndo')


class Aluno(Pessoa):
    def estudar(self):
        print(self.nome, 'está estudando')


class Cliente(Pessoa):
    def comprar(self):
        print(self.nome, 'está comprando')


class ClienteVIP(Cliente):
    def __init__(self, nome, idade, idcliente):
        super().__init__(nome, idade)
        self.id = idcliente

    def atributos(self):
        print(self.nome, self.idade, self.id)


if __name__ == '__main__':
    a1 = Aluno('Marco', 19)
    a1.correr()

    cvip1 = ClienteVIP('Marco', 18, 1)

    cvip1.comprar()

    cvip1.atributos()

