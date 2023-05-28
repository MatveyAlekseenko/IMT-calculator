from PyQt5.QtCore import Qt, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont# проверка типов вводимых значений
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, \
    QGridLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit

from data import *


class FinalWin(QWidget):
    def __init__(self, exp):
        ''' окно, в котором проводится опрос '''
        super().__init__()

        #получаем данные об эксперименте
        self.exp = exp

        # создаём и настраиваем графические элементы:
        self.initUI()

        #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()

        # старт:
        self.show()

    def results(self):
        self.index = (int(self.exp.t1) * (int(self.exp.t1))) / (int(self.exp.t2))

    def initUI(self):
        self.work_text = QLabel(result + self.results())
        self.index_text = QLabel(IMT)

        self.layout_line = QVBoxLayout
        self.layout_line.addWidget(self.work_text, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.index_text,alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)

    def set_appear(self):
        self.setWindowTitle(Title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
