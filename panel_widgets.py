from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QToolBar, QHBoxLayout
from PyQt6.QtCore import QSize, Qt
import sys
from screeninfo import get_monitors
from pynput import keyboard

class MATButton(QPushButton):
    def __init__(self, layout):
        super().__init__("M.A.T.")

        # Sets the dimensions of the button
        self.setFixedWidth(int(layout.width() * 0.10))
        self.setFixedHeight(int(layout.height() * 0.5))