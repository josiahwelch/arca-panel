import copy
import subprocess
import threading

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
        self.entries = []
        self.entries_exec = {}

        # Sets proper flags for the window
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

        # Sets up the scroll bar
        scroll_bar = QScrollBar(self)
        scroll_bar.setStyleSheet("background : gray;")
        self.setVerticalScrollBar(scroll_bar)

        # Configures application clicking
        self.itemClicked.connect(self.item_clicked)

        # Populates the M.A.T. menu
        self.update()

    def _update_from_dir(self):
        applications_dir = '/usr/share/applications'
        self.entries = []
        for file in os.scandir(applications_dir):
            if file.is_file():
                desktop = DesktopFile(file.path)
                self.entries.append(copy.deepcopy(desktop.data))
                print(self.entries[-1])
                try:
                    self.entries_exec[str(self.entries[-1]['Desktop Entry']['Name'])] = self.entries[-1]['Desktop Entry']['Exec']
                except TypeError:
                    self.entries_exec[str(self.entries[-1]['Desktop Entry']['Name'])] = self.entries[-1]['Desktop Entry']['Exec']
                except KeyError as e:
                    # print(f"{e}: {next(iter(self.entries)).data['Desktop Entry']['Name']}")
                    try:
                        self.entries_exec[str(self.entries[-1]['Desktop Entry']['Name']['C'])] = self.entries[-1]['Desktop Entry']['Exec']
                    except KeyError as e:
                        self.entries_exec[str(self.entries[-1]['Desktop Entry']['Name'])] = ""
        for entry in self.entries:
            print(entry)

    def _update_menu(self):
        self.clear()
        for entry in self.entries:
            print(entry['Desktop Entry']['Name'])
            try:
                self.addItem(QListWidgetItem(entry['Desktop Entry']['Name']))
            except TypeError:
                self.addItem(QListWidgetItem(entry['Desktop Entry']['Name']['C']))

    def update(self):
        self._update_from_dir()
        self._update_menu()

    def item_clicked(self, item):
        print(f"item: \"{item.text()}\"")
        print(f"exec: \"{self.entries_exec[item.text()]}\"")
        t = threading.Thread(target=misc_helper.run_command, args=(self.entries_exec[item.text()], ))
        # misc_helper.run_command(self.entries_exec[item.text()])
        t.start()
        self.clearSelection()
        self.hide()


