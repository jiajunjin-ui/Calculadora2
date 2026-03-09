from PySide6 import QtWidgets

from interfaz import Ui_Dialog


class PantallaCalculadora(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def opera(self):
        pass

    def verifica(self):
        pass

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = PantallaCalculadora()
    window.show()
    sys.exit(app.exec_())