import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget
        self.grid = QGridLayout(self.cw)
        self.btn = QPushButton('Texto do botão')

        self.setCentralWidget(self.cw)

        self.grid.addWidget(self.btn, 0, 0, 1, 1)
        


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
