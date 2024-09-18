import sys
import ctypes  
from PyQt5.QtWidgets import QMainWindow, QLabel, QMessageBox, QPushButton, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, Qt

class TimerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(800, 300, 400, 150)
        self.setWindowTitle("Open Lab Timer")
        self.setWindowIcon(QIcon("logo.png"))
        self.setToolTip("OpenLab")
        
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        self.time_remaining = 7200  
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_label)
        self.timer.start(1000)  

        self.label = QLabel(self)
        self.label.setGeometry(50, 20, 300, 50)
        self.label.setText(self.format_time(self.time_remaining))
        self.label.setStyleSheet("font-size: 20px;")

        # Add the logout button
        self.logout_button = QPushButton("Logout", self)
        self.logout_button.setGeometry(150, 80, 100, 30)
        self.logout_button.clicked.connect(self.logout)

        self.notified_30_minutes = False
        self.msg_box = None

    def format_time(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def update_label(self):
        if self.time_remaining > 0:
            self.time_remaining -= 1
            self.label.setText(self.format_time(self.time_remaining))

            if self.time_remaining == 1800 and not self.notified_30_minutes:
                self.notify_30_minutes_left()
                self.notified_30_minutes = True
        else:
            self.timer.stop()
            self.label.setText("Time's up!")
            self.lock_pc()

    def notify_30_minutes_left(self):
        self.msg_box = QMessageBox()
        self.msg_box.setIcon(QMessageBox.Information)
        self.msg_box.setWindowTitle("Time Alert")
        self.msg_box.setText("30 minutes remaining!")
        self.msg_box.setStandardButtons(QMessageBox.Ok)
        self.msg_box.show()

    def lock_pc(self):
        """Locks the PC (Windows) when the timer ends."""
        ctypes.windll.user32.LockWorkStation()
        self.close()

    def logout(self):
        """Handles the logout action by recording the remaining time and closing the application."""
        remaining_time = self.format_time(self.time_remaining)
        # Save remaining time to a file (or any desired method)
        with open("remaining_time.txt", "w") as file:
            file.write(f"Remaining time at logout: {remaining_time}")

        # Close the application
        self.close()

def start_timer():
    """Creates the timer window and shows it."""
    timer_window = TimerWindow()
    timer_window.show()
    return timer_window


