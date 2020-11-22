import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget
        self.grid = QGridLayout(self.cw)
        self.btn1 = QPushButton('Texto do botão')
        self.btn2 = QPushButton('Outro botão')

        self.setCentralWidget(self.cw)

        self.grid.addWidget(self.btn1, 0, 0, 1, 1)
        self.grid.addWidget(self.btn2, 0, 1, 1, 1)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
