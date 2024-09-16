import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(1200, 300, 700, 700)
    win.setWindowTitle("Open Lab")
    win.setWindowIcon(QIcon("logo.png"))
    win.setToolTip("OpenLab")
    win.show()
    sys.exit(app.exec_())

window()