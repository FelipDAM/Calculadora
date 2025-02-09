'''Importar coses'''
import sys
import os
import PySide6.QtWidgets as qt
import PySide6.QtUiTools as qtu

class CalcApp(qt.QMainWindow):
    '''Clase calc'''
    def __init__(self):
        super().__init__()
        loader = qtu.QUiLoader()
        interface_path = os.path.join(os.path.dirname(__file__), "calculadora.ui")
        self.ui = loader.load(interface_path, None)
        self.contingut = ""
        self.acum = ""
        self.operador = ''
        self.result = ''
        self.ui.Button1.clicked.connect(self.marcar1)
        self.ui.Button2.clicked.connect(self.marcar2)
        self.ui.borrarButton.clicked.connect(self.borrar_tot)
        self.ui.sumaButton.clicked.connect(self.suma)
        self.ui.igualButton.clicked.connect(self.igual)
        self.ui.restaButton.clicked.connect(self.resta)

        self.ui.show()

    def marcar1(self):
        '''metode per marcar el num1'''
        if self.contingut!='0':
            valor_actual = self.contingut
            self.ui.display.display(valor_actual+'1')
            self.contingut= valor_actual+'1'
        else:
            valor_actual = ''
            self.ui.display.display(valor_actual+'1')
            self.contingut= valor_actual+'1'

    def marcar2(self):
        '''metode per marcar el num2'''
        if self.contingut!='0':
            valor_actual = self.contingut
            self.ui.display.display(valor_actual+'2')
            self.contingut= valor_actual+'2'
        else:
            valor_actual = ''
            self.ui.display.display(valor_actual+'2')
            self.contingut= valor_actual+'2'

    def borrar_tot(self):
        '''metode per netejar la pantalla'''
        self.contingut = '0'
        valor_actual = self.contingut
        self.ui.display.display(valor_actual)

    def suma(self):
        '''metode per sumar'''
        self.operador = '+'
        self.acum = self.contingut
        self.ui.display.display('')
        self.contingut=''

    def igual(self):
        '''metode per traure el resultat'''
        if self.operador=='+':
            self.result = int(self.contingut) + int(self.acum)
            self.ui.display.display(str(self.result))
        elif self.operador=='-':
            self.result =  int(self.acum) - int(self.contingut)
            self.ui.display.display(str(self.result))
        self.acum = '0'
        self.contingut = '0'

    def resta(self):
        '''metode per restar'''
        self.operador = '-'
        self.acum = self.contingut
        self.ui.display.display('')
        self.contingut=''


if __name__ == "__main__":
    app = qt.QApplication(sys.argv)
    window = CalcApp()
    sys.exit(app.exec())
