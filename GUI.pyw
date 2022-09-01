import sys
from interfaz2 import *
from PyQt5.QtWidgets import *
from tkinter import messagebox

class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(GUI, self).__init__(parent = parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.botonSalida.clicked.connect(self.verificaRespuestas)
        self.ui.botonLimpiar.clicked.connect(self.limpiar)
        self.ui.botonSalida.clicked.connect(self.verificaRespuestas)

    
    #verificar que las casillas y los box no esten vacios
    def verificaRespuestas(self):
        data = []
        if(self.ui.sexoBox.currentIndex() == 0 or
        self.ui.orientacionBox.currentIndex() == 0 or
        self.ui.identidadBox.currentIndex() == 0 or
        self.ui.aportaBox.currentIndex() == 0 or
        self.ui.morbilidadBox.currentIndex() == 0 or
        self.ui.condicionBox.currentIndex() == 0 or
        self.ui.prevencionBox.currentIndex() == 0 or
        self.ui.bonoBox.currentIndex() == 0 or
        self.ui.autoBox.currentIndex() == 0 or
        self.ui.gpBox.currentIndex() == 0 or
        self.ui.nombretxt.toPlainText() == '' or
        self.ui.edadtxt.toPlainText() == ''):
            messagebox.showerror(message="Verifique que halla llenado todos los datos", title='!!!!!!! AVISO !!!!!!!')
        elif(self.ui.sexoBox.currentIndex() == 1 and
        self.ui.gpBox.currentIndex() == 1):
            messagebox.showerror(message="¿Encerio?, un hombre embarazado :/", title='!!!!!!! AVISO !!!!!!!')
        else:
            data.append(self.ui.sexoBox.currentText())
            data.append(self.ui.orientacionBox.currentText())
            data.append(self.ui.identidadBox.currentText())
            data.append(self.ui.edadtxt.toPlainText())
            data.append(self.ui.aportaBox.currentText())
            data.append(self.ui.autoBox.currentText())
            data.append(self.ui.bonoBox.currentText())
            data.append(self.ui.gpBox.currentText())
            data.append(self.ui.prevencionBox.currentText())
            data.append(self.ui.morbilidadBox.currentText())
            data.append(self.ui.condicionBox.currentText())
            self.ui.Salida.setText(data.__str__())

    def limpiar(self):
        self.ui.sexoBox.setCurrentIndex(0)
        self.ui.orientacionBox.setCurrentIndex(0) 
        self.ui.identidadBox.setCurrentIndex(0)
        self.ui.aportaBox.setCurrentIndex(0)
        self.ui.morbilidadBox.setCurrentIndex(0)
        self.ui.condicionBox.setCurrentIndex(0)
        self.ui.prevencionBox.setCurrentIndex(0)
        self.ui.bonoBox.setCurrentIndex(0)
        self.ui.autoBox.setCurrentIndex(0)
        self.ui.gpBox.setCurrentIndex(0)
        self.ui.nombretxt.setPlainText('')
        self.ui.edadtxt.setPlainText('')
        self.ui.Salida.setText('')



if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    app = GUI()
    app.show()
    sys.exit(aplicacion.exec_())