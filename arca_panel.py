from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt6.QtCore import QSize, Qt
import sys
from screeninfo import get_monitors

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self, monitors):
        super().__init__()
        self.main_monitor = monitors[0]
        button = QPushButton("Press Me!")
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setGeometry(0, 0, 1920, 30)  # Full width, thin
        # Set the central widget of the Window.
        self.setCentralWidget(button)

def __main__():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

if __name__ == "__main__":
    __main__()