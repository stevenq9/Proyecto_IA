import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class interfaz(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("proyecto.ui", self)
        self.botonSalida.clicked.connect(self.boton)
    
    def boton(self):
        self.Salida.setText(self.sexoBox.currentText())
        print(self.sexoBox.currentText())
        print(self.sexoBox.currentIndex())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = interfaz()
    GUI.show()
    sys.exit(app.exec_())