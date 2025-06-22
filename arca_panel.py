from PyQt5.QtWidgets import QToolBar
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QToolBar, QHBoxLayout
from PyQt6.QtCore import QSize, Qt
import sys
from screeninfo import get_monitors
from pynput import keyboard

# Subclass QMainWindow to customize your application's main window
class MainWindow(QWidget):
    def __init__(self, monitors):
        super().__init__()
        self.main_monitor = monitors[0]

        # Initializes the variables
        self.button = QPushButton("test")
        self.layout = QHBoxLayout()

        # Sets the proper panel width
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setGeometry(0, 0, self.main_monitor.width, 30)  # Full width, thin

        # Sets up test button
        self.button.setFixedWidth(int(self.width() * 0.10))
        # self.button.setStyleSheet("border: 1px solid #ffffff; background-color: #333333;")

        # Sets up the QHBoxLayout()
        self.layout.setSpacing(155555)
        self.layout.addWidget(self.button)
        self.layout.addStretch()
        self.setLayout(self.layout)

    def key_handler(self, key):
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys
        print(k)

def __main__():
    app = QApplication(sys.argv)

    monitors = get_monitors()
    window = MainWindow(monitors)
    window.show()
    listener = keyboard.Listener(on_press=window.key_handler)
    listener.start()  # start to listen on a separate thread
    app.exec()
    listener.join()  # remove if main thread is polling self.keys

if __name__ == "__main__":
    __main__()