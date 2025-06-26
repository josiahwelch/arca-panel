from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QToolBar, QHBoxLayout
from PyQt6.QtCore import QSize, Qt
import sys
from screeninfo import get_monitors
from pynput import keyboard
from panel_widgets import MATButton

# Subclass QMainWindow to customize your application's main window
class MainWindow(QWidget):
    def __init__(self, monitors):
        super().__init__()
        self.main_monitor = monitors[0]

        # Initializes the variables
        self.layout = QHBoxLayout()
        self.mat_button = MATButton()

        # Sets the proper panel width
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setGeometry(0, 0, self.main_monitor.width, int(self.main_monitor.height * 0.05))  # Full width, thin

        # Sets the dimensions of the M.A.T. button
        self.mat_button.setFixedWidth(int(self.width() * 0.10))
        self.mat_button.setFixedHeight(int(self.height() * 0.5))

        # Sets the dimensions of the M.A.T. menu
        self.mat_button.mat_menu.setGeometry(0, self.height(), int(self.main_monitor.width * 0.25), int(self.main_monitor.height * 0.5))  # Full width, thin

        # Sets up the QHBoxLayout()
        self.layout.setSpacing(5)
        self.layout.addWidget(self.mat_button)
        self.layout.addStretch()
        self.setLayout(self.layout)

    def key_handler(self, key):
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys
        print(k)
        if k == 'alt':
            self.mat_button.mat_pressed()
        elif k == 'b':
            print(self.mat_button.mat_menu.currentItem())

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