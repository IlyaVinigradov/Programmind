from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


class MainWin(QWidget):
    def __init__(self):
        """ конструктор для запуска окна """
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        """ метод для формирования окна """
        # создание названия окна
        self.setWindowTitle('My time')
        # размеры окна
        self.resize(500, 300)
        # цвет заднего фона
        self.setStyleSheet("background-color: rgb(207, 208, 118)")
        # координаты появления окна
        self.move(200, 100)

    def initUI(self):
        """ внешний вид окна 
        4 кнопки: добавить/удалить/обновить/получить(посмотреть результат)
        """
        self.btn_add = QPushButton('Добавить часы')
        self.btn_remove = QPushButton('Удалить часы за день')
        self.btn_update = QPushButton('Обновить часы за день')
        self.btn_show = QPushButton('Показать отработанные часы')

        # создание лэйаута (направляющей линии, где будут наши виджеты (кнопки, текст и тд))
        self.v_layout = QVBoxLayout()
        # добавление виджетов на направляющие линии и расположение
        self.v_layout.addWidget(
            self.btn_add, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v_layout.addWidget(
            self.btn_remove, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v_layout.addWidget(
            self.btn_update, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v_layout.addWidget(
            self.btn_show, alignment=Qt.AlignmentFlag.AlignCenter)
        # добавление виджета на экран
        self.setLayout(self.v_layout)

    def connects(self):
        """ метод для перехода по кнопке к новому экрану """
        pass


app = QApplication([])
mw = MainWin()
app.exec()
# help(MainWin)
