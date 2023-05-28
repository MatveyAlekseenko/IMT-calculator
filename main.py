from PyQt5.QtCore import Qt, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QHBoxLayout, QLineEdit, QGridLayout, QGroupBox, QRadioButton, QListWidget

from data import *
from NewWin import *



class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        #устанавливает, как будет выглядеть окно(надпись, размер, место)
        self.set_appear()
        #Создаем и настраиваем графические элементы:
        self.initUI()
        #Устанавливает связи между элементами
        self.connects()
        #старт:
        self.show()

    def initUI(self):
        self.button_next = QPushButton(button1)
        self.headline = QLabel(headline)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.headline, alignment= Qt.AlignCenter)
        self.layout.addWidget(self.button_next, alignment= Qt.AlignCenter)
        self.setLayout(self.layout)

    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def connects(self):
        self.button_next.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle(Title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
def main():
    app = QApplication([])
    mw = MainWin()
    app.exec_()

main()
