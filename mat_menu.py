from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QToolBar, QHBoxLayout, QVBoxLayout, QLabel, \
    QBoxLayout
from PyQt6.QtCore import QSize, Qt
import sys, os, misc_helper
from screeninfo import get_monitors
from pynput import keyboard
from desktop_parser import DesktopFile

class MATMenu(QWidget):
    def __init__(self):
        super().__init__()

        # Initializes variables
        self.entries = set()
        self.layout = QVBoxLayout()

        # Sets proper flags for the window
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

        # Populates the M.A.T. menu
        self.update()
        self.setLayout(self.layout)

    def _update_from_dir(self):
        applications_dir = '/usr/share/applications'
        for file in os.scandir(applications_dir):
            if file.is_file():
                self.entries.add(DesktopFile(file.path))
                print(file.path)
    def _update_menu(self):
        misc_helper.remove_widgets(self.layout)
        for entry in self.entries:
            self.layout.addWidget(QPushButton(entry.data['Desktop Entry']['Name']))
        self.layout.activate()

    def update(self):
        self._update_from_dir()
        self._update_menu()



