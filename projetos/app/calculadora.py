import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        # customização dos botões
        self.btn1 = QPushButton('1')
        self.btn2 = QPushButton('2')
        self.btn3 = QPushButton('3')
        self.btn4 = QPushButton('4')
        self.btn5 = QPushButton('5')
        self.btn6 = QPushButton('6')
        self.btn7 = QPushButton('7')
        self.btn8 = QPushButton('8')
        self.btn9 = QPushButton('9')
        self.btn0 = QPushButton('0')
        self.btnsom = QPushButton('+')
        self.btnsub = QPushButton('-')
        self.btnmul = QPushButton('*')
        self.btndiv = QPushButton('/')
        self.btnponto = QPushButton('.')
        self.btnigual = QPushButton('=')
        self.btnC = QPushButton('C')

        # função dos botões
        self.btn1.clicked.connect(self.botao1)
        self.btn2.clicked.connect(self.botao2)
        self.btn3.clicked.connect(self.botao3)
        self.btn4.clicked.connect(self.botao4)
        self.btn5.clicked.connect(self.botao5)
        self.btn6.clicked.connect(self.botao6)
        self.btn7.clicked.connect(self.botao7)
        self.btn8.clicked.connect(self.botao8)
        self.btn9.clicked.connect(self.botao9)
        self.btn0.clicked.connect(self.botao0)
        self.btnsom.clicked.connect(self.botaosoma)
        self.btnsub.clicked.connect(self.botaosubtracao)
        self.btnmul.clicked.connect(self.botaomultip)
        self.btndiv.clicked.connect(self.botaodivisao)
        self.btnponto.clicked.connect(self.botaoponto)
        self.btnigual.clicked.connect(self.botaoigual)
        self.btnC.clicked.connect(self.botaoC)

        self.setCentralWidget(self.cw)

        # grade
        self.grid.addWidget(self.btn1, 2, 0, 1, 1)
        self.grid.addWidget(self.btn2, 2, 1, 1, 1)
        self.grid.addWidget(self.btn3, 2, 2, 1, 1)
        self.grid.addWidget(self.btn4, 1, 0, 1, 1)
        self.grid.addWidget(self.btn5, 1, 1, 1, 1)
        self.grid.addWidget(self.btn6, 1, 2, 1, 1)
        self.grid.addWidget(self.btn7, 0, 0, 1, 1)
        self.grid.addWidget(self.btn8, 0, 1, 1, 1)
        self.grid.addWidget(self.btn9, 0, 2, 1, 1)
        self.grid.addWidget(self.btn0, 3, 0, 1, 2)
        self.grid.addWidget(self.btnsom, 0, 3, 1, 1)
        self.grid.addWidget(self.btnsub, 1, 3, 1, 1)
        self.grid.addWidget(self.btnmul, 2, 3, 1, 1)
        self.grid.addWidget(self.btndiv, 3, 3, 1, 1)
        self.grid.addWidget(self.btnponto, 3, 2, 1, 1)
        self.grid.addWidget(self.btnigual, 2, 4, 2, 2)
        self.grid.addWidget(self.btnC, 0, 4, 2, 2)

    def botao1(self):
        pass

    def botao2(self):
        pass

    def botao3(self):
        pass

    def botao4(self):
        pass

    def botao5(self):
        pass

    def botao6(self):
        pass

    def botao7(self):
        pass

    def botao8(self):
        pass

    def botao9(self):
        pass

    def botao0(self):
        pass

    def botaosoma(self):
        pass

    def botaosubtracao(self):
        pass

    def botaomultip(self):
        pass

    def botaodivisao(self):
        pass

    def botaoponto(self):
        pass

    def botaoigual(self):
        pass

    def botaoC(self):
        pass


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
