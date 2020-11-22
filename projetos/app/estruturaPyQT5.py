import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.btn1 = QPushButton('Print A')
        self.btn2 = QPushButton('Print B')
        self.btn3 = QPushButton('Print C')
        self.btn4 = QPushButton('Print D')
        self.btn_espaco = QPushButton('Pular linha')

        self.btn1.clicked.connect(self.botao1)
        self.btn2.clicked.connect(self.botao2)
        self.btn3.clicked.connect(self.botao3)
        self.btn4.clicked.connect(self.botao4)
        self.btn_espaco.clicked.connect(self.botao_espaco)

        self.setCentralWidget(self.cw)

        self.grid.addWidget(self.btn1, 0, 0, 1, 1)
        self.grid.addWidget(self.btn2, 0, 1, 1, 1)
        self.grid.addWidget(self.btn3, 1, 0, 1, 1)
        self.grid.addWidget(self.btn4, 1, 1, 1, 1)
        self.grid.addWidget(self.btn_espaco, 2, 0, 1, 2)

    def botao1(self):
        print('A')

    def botao2(self):
        print('B')

    def botao3(self):
        print('C')

    def botao4(self):
        print('D')

    def botao_espaco(self):
        print()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
