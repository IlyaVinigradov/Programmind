from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget


class Main_Win(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle('Мой калькулятор')
        self.setGeometry(200, 100, 300, 400)

    def initUI(self):
        # надпись
        res = QLabel()
        # кнопка
        btn1 = QPushButton('1')
        btn2 = QPushButton('2')
        btn3 = QPushButton('3')
        btn4 = QPushButton('4')
        # направляющие линии
        v_line = QVBoxLayout()
        h_line = QHBoxLayout()
        # добавляем виджеты на направляющие линии
        h_line.addWidget(btn1, alignment=Qt.AlignmentFlag.AlignRight)
        h_line.addWidget(btn2, alignment=Qt.AlignmentFlag.AlignCenter)
        h_line.addWidget(btn3, alignment=Qt.AlignmentFlag.AlignLeft)
        v_line.addWidget(res, alignment=Qt.AlignmentFlag.AlignHCenter)
        v_line.addLayout(h_line)
        self.setLayout(v_line)
