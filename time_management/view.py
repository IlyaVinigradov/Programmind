from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


class View(QMainWindow):
    """ Класс View, который отвечает только за внешний вид экрана """

    def __init__(self):
        super().__init__()
        # главный экран виджет, для удобного прехода между окнами
        self.main_win = QStackedWidget()
        # сделать main_win главным экраном
        self.setCentralWidget(self.main_win)
        # self.main_win_ui()
        self.add_screen_ui()
        self.set_appear()
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

    def main_win_ui(self):
        """ внешний вид окна 
        2 кнопки: добавить/удалить/обновить и посмотреть результат
        """
        self.btn_add = QPushButton('Добавить часы')
        self.btn_show = QPushButton('Показать отработанные часы')

        # создание лэйаута (направляющей линии, где будут наши виджеты (кнопки, текст и тд))
        self.layout_widget = QWidget()
        self.v_layout = QVBoxLayout(self.layout_widget)
        # добавление виджетов на направляющие линии и расположение
        self.v_layout.addWidget(
            self.btn_add, alignment=Qt.AlignmentFlag.AlignCenter)
        self.v_layout.addWidget(
            self.btn_show, alignment=Qt.AlignmentFlag.AlignCenter)
        # добавление виджета на экран
        self.main_win.addWidget(self.layout_widget)

    def add_screen_ui(self):
        """ метод для отображения второго экрана по добавлению времени """
        # надпись
        self.input_time = QLabel('Введите время')
        # поле ввода
        self.my_time = QSpinBox()
        # задаю минимальный диапазон
        self.my_time.setMinimum(0)
        # выбор дня
        self.day = QLabel('выберите день')
        # календарь
        self.cal = QCalendarWidget()
        self.cal.setGridVisible(True)
        self.cal.resize(310, 200)

        self.cal.clicked[QDate].connect(self.showDate)
        # выбор дня
        self.lbl = QLabel()
        # сообщение для наглядности
        self.result_label = QLabel()
        self.result_label.setText(
            f'вы выбрали {self.lbl} и {self.my_time.value()} часов')

        # кнопка для сохранения
        self.btn_save = QPushButton('Сохранить')
        # кнопка назад
        self.btn_back = QPushButton('Назад')

        # лэйаут для расположения виджетов на экране
        self.layout_widget = QWidget()
        self.c_line = QVBoxLayout()
        self.bottom_h_line = QHBoxLayout()
        self.c_line.addWidget(
            self.input_time, alignment=Qt.AlignmentFlag.AlignCenter)
        self.c_line.addWidget(
            self.my_time, alignment=Qt.AlignmentFlag.AlignCenter)
        self.c_line.addWidget(self.day, alignment=Qt.AlignmentFlag.AlignCenter)
        self.c_line.addWidget(self.cal, alignment=Qt.AlignmentFlag.AlignCenter)
        self.c_line.addWidget(
            self.result_label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.bottom_h_line.addWidget(
            self.btn_save, alignment=Qt.AlignmentFlag.AlignRight)
        self.bottom_h_line.addWidget(
            self.btn_back, alignment=Qt.AlignmentFlag.AlignLeft)
        self.c_line.addLayout(self.bottom_h_line)
        self.layout_widget.setLayout(self.c_line)
        self.main_win.addWidget(self.layout_widget)

    # Применение стилей к календарю
    calendar_style = """
        QCalendarWidget QAbstractItemView {
            selection-background-color: rgb(207, 208, 118);
        }
        QCalendarWidget QWidget#qt_calendar_navigationbar {
            background-color: rgb(207, 208, 118);
        }
        QCalendarWidget QToolButton {
            padding: 5px;
        }
    """

    def showDate(self, date):
        self.lbl.setText(date.toString())
