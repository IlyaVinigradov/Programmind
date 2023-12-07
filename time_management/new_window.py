# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.stacked_widget = QStackedWidget()
#         self.setCentralWidget(self.stacked_widget)

#         self.screen1_button = QPushButton('Открыть новый экран')
#         self.screen1_button.clicked.connect(self.open_screen2)

#         screen1_layout = QVBoxLayout()
#         screen1_layout.addWidget(self.screen1_button)

#         screen1_widget = QWidget()
#         screen1_widget.setLayout(screen1_layout)

#         self.stacked_widget.addWidget(screen1_widget)

#     def open_screen2(self):
#         self.screen2_button = QPushButton('Вернуться назад')
#         self.screen2_button.clicked.connect(self.open_screen1)

#         screen2_layout = QVBoxLayout()
#         screen2_layout.addWidget(self.screen2_button)

#         screen2_widget = QWidget()
#         screen2_widget.setLayout(screen2_layout)

#         self.stacked_widget.addWidget(screen2_widget)
#         self.stacked_widget.setCurrentWidget(screen2_widget)

#     def open_screen1(self):
#         self.stacked_widget.setCurrentIndex(0)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.screen1_button = QPushButton('Открыть экран 2')
        self.screen1_button.clicked.connect(self.open_screen2)

        screen1_button2 = QPushButton('Открыть экран 3')
        screen1_button2.clicked.connect(self.open_screen3)

        screen1_layout = QVBoxLayout()
        screen1_layout.addWidget(self.screen1_button)
        screen1_layout.addWidget(screen1_button2)

        screen1_widget = QWidget()
        screen1_widget.setLayout(screen1_layout)
        self.stacked_widget.addWidget(screen1_widget)

    def open_screen2(self):
        self.screen2_button = QPushButton('Вернуться на экран 1')
        self.screen2_button.clicked.connect(self.open_screen1)

        screen2_button2 = QPushButton('Открыть экран 3')
        screen2_button2.clicked.connect(self.open_screen3)

        screen2_layout = QVBoxLayout()
        screen2_layout.addWidget(self.screen2_button)
        screen2_layout.addWidget(screen2_button2)

        screen2_widget = QWidget()
        screen2_widget.setLayout(screen2_layout)

        self.stacked_widget.addWidget(screen2_widget)
        self.stacked_widget.setCurrentWidget(screen2_widget)

    def open_screen3(self):
        self.screen3_button = QPushButton('Вернуться на экран 1')
        self.screen3_button.clicked.connect(self.open_screen1)

        screen3_button2 = QPushButton('Вернуться на экран 2')
        screen3_button2.clicked.connect(self.open_screen2)

        screen3_layout = QVBoxLayout()
        screen3_layout.addWidget(self.screen3_button)
        screen3_layout.addWidget(screen3_button2)

        screen3_widget = QWidget()
        screen3_widget.setLayout(screen3_layout)

        self.stacked_widget.addWidget(screen3_widget)
        self.stacked_widget.setCurrentWidget(screen3_widget)

    def open_screen1(self):
        self.stacked_widget.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
