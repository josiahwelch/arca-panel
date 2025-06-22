from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QToolBar, QHBoxLayout
from PyQt6.QtCore import QSize, Qt
import sys
from screeninfo import get_monitors
from pynput import keyboard

class MATButton(QPushButton):
    def __init__(self, widget):
        super().__init__("M.A.T.")

        # Sets the dimensions of the button
        self.setFixedWidth(int(widget.width() * 0.10))
        self.setFixedHeight(int(widget.height() * 0.5))