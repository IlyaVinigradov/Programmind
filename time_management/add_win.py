from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


class AddWin(QWidget):
    """ класс - экран по добавлению времени """

    def __init__(self):
        """ конструктор для запуска второго окна """
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
        pass

    def connects(self):
        pass


if __name__ == '__main__':
    help(AddWin)
