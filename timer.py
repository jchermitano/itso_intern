from PyQt5.QtWidgets import QMainWindow, QLabel, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer

class TimerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window setup
        self.setGeometry(800, 300, 400, 100)
        self.setWindowTitle("Open Lab Timer")
        self.setWindowIcon(QIcon("logo.png"))
        self.setToolTip("OpenLab")

        # Countdown timer setup (2 hours = 7200 seconds)
        self.time_remaining = 1803  # For testing, set to a short time
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_label)
        self.timer.start(1000)  # Start the timer with a 1-second interval

        # Label to display the time
        self.label = QLabel(self)
        self.label.setGeometry(50, 20, 300, 50)
        self.label.setText(self.format_time(self.time_remaining))
        self.label.setStyleSheet("font-size: 20px;")

        # Flag to notify when the 30-minute mark is reached
        self.notified_30_minutes = False

        # Hold the message box as an instance variable to keep it in memory
        self.msg_box = None

    def format_time(self, seconds):
        """Convert seconds to HH:MM:SS format."""
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def update_label(self):
        """Update the QLabel with the remaining time and notify when 30 minutes are left."""
        if self.time_remaining > 0:
            self.time_remaining -= 1
            self.label.setText(self.format_time(self.time_remaining))

            # Notify at the 30-minute mark (1800 seconds)
            if self.time_remaining == 1800 and not self.notified_30_minutes:
                self.notify_30_minutes_left()
                self.notified_30_minutes = True
        else:
            self.timer.stop()
            self.label.setText("Time's up!")

    def notify_30_minutes_left(self):
        """Show popup notification when 30 minutes are left."""
        self.msg_box = QMessageBox()
        self.msg_box.setIcon(QMessageBox.Information)
        self.msg_box.setWindowTitle("Time Alert")
        self.msg_box.setText("30 minutes remaining!")
        self.msg_box.setStandardButtons(QMessageBox.Ok)
        self.msg_box.show()

def start_timer():
    """Creates the timer window and shows it."""
    timer_window = TimerWindow()
    timer_window.show()
    return timer_window
