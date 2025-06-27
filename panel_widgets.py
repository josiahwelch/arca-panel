import threading
import time
from datetime import datetime

import pytz
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QToolBar, QHBoxLayout, QLabel
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

class TimeWidget(QLabel):
    def __init__(self, region=None, city=None):
        super().__init__("TIME INIT")

        # Initialize variables
        self.thread = threading.Thread(target=self._time_get)
        self.current_time = None
        self.font = QFont()
        if region is None:
            self.region = "America"
            self.city = "Chicago"
        else:
            self.region = region
            self.city = city

        # Sets font size
        self.font.setPointSize(12)
        self.setFont(self.font)

    def start(self):
        self.thread.start()

    def stop(self):
        self.thread.join()

    def set_timezone(self, region, city):
        self.region = region
        self.city = city

    def get_timezone(self):
        return f"{self.region}/{self.city}"

    def _time_get(self):
        while True:
            tz = pytz.timezone(self.get_timezone())
            self.current_time = datetime.now(tz)
            self.setText(self.current_time.strftime("%H:%M"))
            # print(f"Current time in {self.city}:", self.current_time.strftime("%H:%M"))
            time.sleep(1)