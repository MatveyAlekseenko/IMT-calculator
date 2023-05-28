from PyQt5.QtCore import Qt, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, \
    QGridLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit

from data import *
from finalwin import *


class Experiment():
    def __init__(self, height, weight):
        self.t1 = height
        self.t2 = weight

class TestWin(QWidget):
    def __init__(self):
        ''' окно, в котором проводится опрос '''
        super().__init__()

        # создаём и настраиваем графические элементы:
        self.initUI()

        #устанавливает связи между элементами
        self.connects()

        #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()

        # старт:
        self.show()

    def set_appear(self):
        self.setWindowTitle(Title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.button2 = QPushButton(button2, self)

        self.firstinput = QLabel(firstinput, self)
        self.secondinput = QLabel(secondinput, self)
        self.info1 = QLabel(info1, self)
        self.info2 = QLabel(info2, self)

        self.line_test1 = QLineEdit(line_test, self)
        self.line_test2 = QLineEdit(line_test, self)

        self.v_line = QVBoxLayout()
        self.v_line.addWidget(info1, alignment= Qt.AlignCenter)
        self.v_line.addWidget(firstinput, alignment=Qt.AlignLeft)
        self.v_line.addWidget(line_test, alignment=Qt.AlignLeft)
        self.v_line.addWidget(secondinput, alignment=Qt.AlignLeft)
        self.v_line.addWidget(line_test, alignment=Qt.AlignLeft)
        self.v_line.addWidget(info2, alignment=Qt.AlignCenter)
        self.v_line.addWidget(button2, alignment=Qt.AlignCenter)
        self.v_line.addWidget(self.v_line)
        self.setLayout(self.v_line)

    def next_click(self):
        self.hide()
        self.exp = Experiment(int(self.line_test1.text()), self.line_test2.text())
        self.fw = FinalWin(self.exp)

    def connects(self):
        self.button_next.clicked.connect(self.next_click)
