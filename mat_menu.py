from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QToolBar, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import QSize, Qt
import sys, os
from screeninfo import get_monitors
from pynput import keyboard
from desktop_parser import DesktopFile

class MatMenu(QVBoxLayout):
    def __init__(self):
        super().__init__()

        # Initializes variables
        self.entries = set()

        self.update()
        print(len(self.entries))

    def update(self):
        applications_dir = "/usr/share/applications"
        for file in os.scandir(applications_dir):
            if file.is_file():
                self.entries.add(DesktopFile(file.path))


