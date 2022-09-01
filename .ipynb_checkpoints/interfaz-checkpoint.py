import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class interfaz(QmainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('proyecto.ui', self)
        