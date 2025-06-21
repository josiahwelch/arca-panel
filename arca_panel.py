from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt6.QtCore import QSize, Qt
import sys
from screeninfo import get_monitors
from pynput import keyboard

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self, monitors):
        super().__init__()
        self.main_monitor = monitors[0]
        self.button = QPushButton("Press Me!")

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setGeometry(0, 0, self.main_monitor.width, 30)  # Full width, thin
        # Set the central widget of the Window.
        self.setCentralWidget(self.button)

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