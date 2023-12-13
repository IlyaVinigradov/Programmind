from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


class Main_Win(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle('Мой калькулятор')
        self.setGeometry(200, 100, 100, 200)

    def initUI(self):
        # надпись
        res = QLabel('пример')
        # кнопка
        btnres = QPushButton('=')
        btn1 = QPushButton('1')
        btn2 = QPushButton('2')
        btn3 = QPushButton('3')
        btn4 = QPushButton('4')
        btn5 = QPushButton('5')
        btn6 = QPushButton('6')
        btn7 = QPushButton('7')
        btn8 = QPushButton('8')
        btn9 = QPushButton('9')
        btn0 = QPushButton('0')
        btndot = QPushButton('.')
        btndel = QPushButton('<-')
        btnmult = QPushButton('*')
        btndiv = QPushButton('/')
        btndiff = QPushButton('-')
        btnsum = QPushButton('+')
        # направляющие линии
        v_line = QVBoxLayout()
        h_line = QHBoxLayout()
        h_line1 = QHBoxLayout()
        h_line2 = QHBoxLayout()
        h_line3 = QHBoxLayout()
        h_line4 = QHBoxLayout()
        # добавляем виджеты на направляющие линии
        h_line.addWidget(res, alignment=Qt.AlignmentFlag.AlignLeft)
        h_line.addWidget(btnsum, alignment=Qt.AlignmentFlag.AlignRight)

        h_line1.addWidget(btn1, alignment=Qt.AlignmentFlag.AlignRight)
        h_line1.addWidget(btn2, alignment=Qt.AlignmentFlag.AlignCenter)
        h_line1.addWidget(btn3, alignment=Qt.AlignmentFlag.AlignLeft)
        h_line1.addWidget(btnmult, alignment=Qt.AlignmentFlag.AlignCenter)

        h_line2.addWidget(btn4, alignment=Qt.AlignmentFlag.AlignRight)
        h_line2.addWidget(btn5, alignment=Qt.AlignmentFlag.AlignCenter)
        h_line2.addWidget(btn6, alignment=Qt.AlignmentFlag.AlignLeft)
        h_line2.addWidget(btndiv, alignment=Qt.AlignmentFlag.AlignCenter)

        h_line3.addWidget(btn7, alignment=Qt.AlignmentFlag.AlignRight)
        h_line3.addWidget(btn8, alignment=Qt.AlignmentFlag.AlignCenter)
        h_line3.addWidget(btn9, alignment=Qt.AlignmentFlag.AlignLeft)
        h_line3.addWidget(btndiff, alignment=Qt.AlignmentFlag.AlignCenter)

        h_line4.addWidget(btn0, alignment=Qt.AlignmentFlag.AlignCenter)
        h_line4.addWidget(btndot, alignment=Qt.AlignmentFlag.AlignCenter)
        h_line4.addWidget(btndel, alignment=Qt.AlignmentFlag.AlignRight)
        h_line4.addWidget(btnres, alignment=Qt.AlignmentFlag.AlignCenter)

        v_line.addLayout(h_line)
        v_line.addLayout(h_line1)
        v_line.addLayout(h_line2)
        v_line.addLayout(h_line3)
        v_line.addLayout(h_line4)
        self.setLayout(v_line)
