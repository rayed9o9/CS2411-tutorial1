import sys
from PyQt5 import QtWidgets, uic

class ExampleApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('my_ui.ui', self)
        # Connect signals and slots here

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
