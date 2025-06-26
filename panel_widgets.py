from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QToolBar, QHBoxLayout
from PyQt6.QtCore import QSize, Qt
import sys
from screeninfo import get_monitors
from pynput import keyboard
from mat_menu import MATMenu

class MATButton(QPushButton):
    def __init__(self):
        super().__init__("M.A.T.")

        # Initializes variables
        self.mat_menu = MATMenu()
        self.is_mat_shown = False

        # Sets up button listener
        self.clicked.connect(self.pressed)

    def pressed(self):
        if self.is_mat_shown:
            self.mat_menu.hide()
            self.is_mat_shown = False
        else:
            self.mat_menu.show()
            self.is_mat_shown = True

class LogoutButton(QPushButton):
    def __init__(self, func=None):
        super().__init__("Logout")

        # Sets up button listener
        self.clicked.connect(self.pressed)

    def pressed(self):
        print("UNBOUND YET")
