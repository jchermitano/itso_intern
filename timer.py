import sys
import ctypes  # For locking the workstation on Windows
from PyQt5.QtWidgets import QMainWindow, QLabel, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, Qt

class TimerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window setup
        self.setGeometry(800, 300, 400, 100)
        self.setWindowTitle("Open Lab Timer")
        self.setWindowIcon(QIcon("logo.png"))
        self.setToolTip("OpenLab")
        
        # Always keep this window on top
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        self.time_remaining = 7200  # For testing, set to a short time
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_label)
        self.timer.start(1000)  # Start the timer with a 1-second interval

        self.label = QLabel(self)
        self.label.setGeometry(50, 20, 300, 50)
        self.label.setText(self.format_time(self.time_remaining))
        self.label.setStyleSheet("font-size: 20px;")

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
        # Close the application after locking the PC
        self.close()

def start_timer():
    """Creates the timer window and shows it."""
    timer_window = TimerWindow()
    timer_window.show()
    return timer_window
