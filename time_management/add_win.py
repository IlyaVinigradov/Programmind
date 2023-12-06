from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
import json
import os
from pathlib import Path
from datetime import datetime
from main import MainWin


# читаем файл
DIR = Path(__file__).resolve().parent  # путь до текущей папки
# print(DIR)
os.chdir(DIR)  # перейти в папку по пути


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
        # цвет заднего фона
        self.setStyleSheet("background-color: rgb(207, 208, 118)")
        # один метод для размеров экрана и появления в координатах
        # setGeometry(x, y, width, height)
        self.setGeometry(200, 129, 500, 300)

    def initUI(self):
        # надпись
        self.label = QLabel('Введите отработанное время')
        # поле ввода
        self.my_time = QSpinBox()
        # задаю минимальный диапазон
        self.my_time.setMinimum(0)
        # кнопка для сохранения
        self.btn_save = QPushButton('Сохранить')
        # кнопка назад
        self.btn_back = QPushButton('Назад')

        # лэйаут для расположения виджетов на экране
        self.c_line = QVBoxLayout()
        self.c_line.addWidget(
            self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.c_line.addWidget(
            self.my_time, alignment=Qt.AlignmentFlag.AlignCenter)
        self.c_line.addWidget(
            self.btn_save, alignment=Qt.AlignmentFlag.AlignCenter)
        self.c_line.addWidget(
            self.btn_back, alignment=Qt.AlignmentFlag.AlignLeft)
        self.setLayout(self.c_line)

    def connects(self):
        """ метод нажатие на кнопку т.е. сохранение и назад"""
        self.btn_save.clicked.connect(self.final_move)
        self.btn_back.clicked.connect(self.back)

    def save(self):
        """ метод записи в json файл """
        # создаем словарь
        self.data = {}
        # добавляем ключ и словарь в значение
        self.data['work'] = {}
        # обработка исключений
        try:
            # открытие файла в режиме чтения
            with open('my work time.json', 'r') as file:
                # загрузка файла в список
                self.data = json.load(file)
        except FileNotFoundError:
            pass
        self.data['work'][datetime.today()] = self.my_time.value()
        with open(DIR / 'my work time.json', 'w') as file:
            json.dump(self.data, file)

    def done(self):
        """ Всплывающее окошко о выполнении """
        self.done_win = QMessageBox()
        self.done_win.setText('Выполнено')
        self.done_win.exec()

    def back(self):
        """ переход на предыдущий экран """
        self.hide()
        self.main = MainWin()

    def final_move(self):
        """ сохранение и оповещение о готовности """
        self.save()
        self.done()


if __name__ == '__main__':
    help(AddWin)
