class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def chamar(self, pessoa):
        print(self.nome + ' chamou ' + pessoa.nome)


p1 = Pessoa('Marco', 18)
p2 = Pessoa('Albert', 20)

p1.chamar(p2)

