import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon

def window():
    app = QApplication(sys.argv)
    global win
    win = QMainWindow()
    win.setGeometry(800, 300, 500, 500)
    win.setWindowTitle("Open Lab")
    win.setWindowIcon(QIcon("logo.png"))
    win.setToolTip("OpenLab")

    # Window dimensions
    window_width = win.width()
    window_height = win.height()

    # Element dimensions
    input_width = 200
    input_height = 30
    button_width = 100
    button_height = 30

    # Calculate positions to center the elements
    x_center = (window_width - input_width) // 2
    y_center = (window_height // 2) - 60

    # Create a QLineEdit for email input with placeholder and rounded corners
    global name_input
    name_input = QLineEdit(win)
    name_input.setPlaceholderText("Enter your Email")
    name_input.setGeometry(x_center, y_center, input_width, input_height)
    name_input.setStyleSheet("border: 2px solid gray; border-radius: 10px; padding: 5px;")

    # Create a QLineEdit for student number input with placeholder and rounded corners
    global student_number_input
    student_number_input = QLineEdit(win)
    student_number_input.setPlaceholderText("Enter your Student Number")
    student_number_input.setGeometry(x_center, y_center + 50, input_width, input_height)
    student_number_input.setStyleSheet("border: 2px solid gray; border-radius: 10px; padding: 5px;")

    # Create a QPushButton with rounded corners
    login_button = QPushButton("Submit", win)
    login_button.setGeometry((window_width - button_width) // 2, y_center + 100, button_width, button_height)
    login_button.setStyleSheet("""
        QPushButton {
            border: 2px solid gray;
            border-radius: 15px;  /* Rounded corners */
            background-color: #A3C1DA;
            padding: 5px;
        }
        QPushButton:hover {
            background-color: #BCD2E8;  /* Slightly lighter when hovered */
        }
    """)

    win.show()
    sys.exit(app.exec_())

window()
