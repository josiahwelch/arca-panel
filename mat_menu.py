from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QToolBar, QHBoxLayout, QVBoxLayout, QLabel, \
    QBoxLayout, QScrollArea, QScrollBar, QListWidget, QListWidgetItem
from PyQt6.QtCore import QSize, Qt
import sys, os, misc_helper
from screeninfo import get_monitors
from pynput import keyboard
from desktop_parser import DesktopFile

class MATMenu(QListWidget):
    def __init__(self):
        super().__init__()

        # Initializes variables
        self.entries = set()
        self.scroll = QScrollArea()

        # Sets proper flags for the window
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

        # Sets up the scroll bar
        scroll_bar = QScrollBar(self)
        scroll_bar.setStyleSheet("background : gray;")
        self.setVerticalScrollBar(scroll_bar)

        # Populates the M.A.T. menu
        self.update()

    def _update_from_dir(self):
        applications_dir = '/usr/share/applications'
        for file in os.scandir(applications_dir):
            if file.is_file():
                self.entries.add(DesktopFile(file.path))
                print(file.path)

    def _update_menu(self):
        self.clear()
        for entry in self.entries:
            self.addItem(QListWidgetItem(entry.data['Desktop Entry']['Name']))

    def update(self):
        self._update_from_dir()
        self._update_menu()



