import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

def window():
    app = QApplication(sys.argv)
    global win
    win = QMainWindow()

    # Get screen dimensions
    screen = app.primaryScreen()
    screen_size = screen.size()
    screen_width = screen_size.width()
    screen_height = screen_size.height()

    # Set window dimensions: width as 30% of screen width, and full screen height
    window_width = int(screen_width * 0.3)
    window_height = screen_height

    # Set window to appear on the right side
    x_position = screen_width - window_width
    win.setGeometry(x_position, 0, window_width, window_height)

    win.setWindowTitle("Open Lab")
    win.setWindowIcon(QIcon("logo.png"))
    win.setToolTip("OpenLab")

    # Element dimensions
    input_width = 200
    input_height = 30
    button_width = 100
    button_height = 30

    # Calculate positions to center the elements horizontally within the window
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
