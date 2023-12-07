from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


class Model():
    def showDate(self, date):
        self.lbl.setText(date.toString())
