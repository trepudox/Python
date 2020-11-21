from abc import ABC, abstractmethod


def pulalinha():
    print()


class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)
        self.conta_corrente = None
        self.conta_poupanca = None


class Conta(ABC):
    @abstractmethod
    def __init__(self, agencia: int, conta: int, saldo: float):
        self.__agencia = agencia
        self.__conta = conta
        self._saldo = round(saldo, 2)

    @abstractmethod
    def sacar(self, valor):
        self._saldo -= valor
        print(f'R$ {valor} foram sacados da conta.')
        self.mostrar_saldo_atual()
        pulalinha()

    @abstractmethod
    def dados_da_conta(self):
        print(f'A agência é: {self.__agencia}\nO número da conta é: {self.__conta}')
        pulalinha()

    def depositar(self, valor):
        self._saldo += valor
        print(f'R$ {valor} foram depositados na conta')
        self.mostrar_saldo_atual()
        pulalinha()

    def mostrar_saldo_atual(self):
        print(f'O saldo atual da conta é de {round(self._saldo, 2)}')
        pulalinha()


class ContaPoupanca(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float):
        super().__init__(agencia, conta, saldo)

    def sacar(self, valor: float):
        if self._saldo >= valor:
            super().sacar(valor)
        else:
            print(f'Impossível sacar R${valor}, saldo insuficiente.')
            self.mostrar_saldo_atual()

    def acrescimo_mensal(self, meses: int):
        print(f'Você possuía {round(self._saldo, 2)}, após {meses} mês/meses, ', end='')
        total = 0
        for x in range(meses):
            conta = self._saldo * 0.025
            self._saldo += conta
            total += conta
        print(f'você obteve um acréscimo de {round(total, 2)}.')
        self.mostrar_saldo_atual()

    def dados_da_conta(self):
        print('Esta é uma conta poupança.')
        super().dados_da_conta()


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float, limite=500):
        super().__init__(agencia, conta, saldo)
        self.__limite = limite

    def sacar(self, valor):
        if self._saldo + self.__limite > valor:
            super().sacar(valor)
        else:
            print(f'Impossível sacar R${valor}, saldo insuficiente.')
            self.mostrar_saldo_atual()

    def dados_da_conta(self):
        print('Esta é uma conta corrente.')
        super().dados_da_conta()


########################################################################################################################
cliente1 = Cliente('Marco', 18)
cliente1.conta_corrente = ContaCorrente(1111, 1111, 6000)
cliente1.conta_poupanca = ContaPoupanca(1111, 1111, 8000)

cliente1.conta_poupanca.dados_da_conta()

cliente1.conta_poupanca.mostrar_saldo_atual()

cliente1.conta_poupanca.acrescimo_mensal(1)
cliente1.conta_poupanca.acrescimo_mensal(3)
cliente1.conta_poupanca.acrescimo_mensal(3)
cliente1.conta_poupanca.acrescimo_mensal(3)

cliente1.conta_poupanca.sacar(1111)
