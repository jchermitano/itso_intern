import sys
import mysql.connector  # For MySQL database connection
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QIntValidator  # Added QIntValidator for input restriction
import re  # For regular expression to validate email
import timer  # Importing timer module

# Database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',  # Replace with your MySQL username
    'password': 'admin',  # Replace with your MySQL password
    'database': 'OpenLabDB'
}

def insert_user(email, student_number):
    """Function to insert email and student_number into MySQL database."""
    try:
        # Establish connection to MySQL database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Insert the user data
        sql_query = "INSERT INTO users (email, student_number) VALUES (%s, %s)"
        cursor.execute(sql_query, (email, student_number))

        # Commit the transaction
        connection.commit()

        cursor.close()
        connection.close()
        return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False

def on_submit():
    email = name_input.text()
    student_number = student_number_input.text()

    # Email validation: Must end with '@tip.edu.ph'
    if not re.match(r'^[\w\.-]+@tip\.edu\.ph$', email):
        QMessageBox.warning(win, "Email Error", "Please enter a valid TIP email.")
        return

    # Student number validation: Must be exactly 7 digits and numeric
    if len(student_number) != 7:
        QMessageBox.warning(win, "Student Number Error", "Please enter a valid Student Number.")
        return

    # Insert the data into the database
    success = insert_user(email, student_number)
    
    if success:
        print(f"Inserted into database: Email: {email}, Student Number: {student_number}")
        # Proceed to start the timer
        global timer_window
        timer_window = timer.start_timer()
    else:
        QMessageBox.critical(win, "Database Error", "Failed to insert data into the database.")

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
    
    # Set QIntValidator to allow only numbers and restrict input to 7 digits
    int_validator = QIntValidator(0, 9999999)  # Limiting to 7 digits
    student_number_input.setValidator(int_validator)

    # Create a QPushButton with rounded corners
    login_button = QPushButton("Submit", win)
    login_button.setGeometry((window_width - button_width) // 2, y_center + 100, button_width, button_height)
    login_button.setStyleSheet("""
        QPushButton {
            border: 2px solid gray;
            border-radius: 15px;
            background-color: #A3C1DA;
            padding: 5px;
        }
        QPushButton:hover {
            background-color: #BCD2E8;
        }
    """)

    # Connect the button's clicked signal to on_submit function
    login_button.clicked.connect(on_submit)

    win.show()
    sys.exit(app.exec_())

window()
