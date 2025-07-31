#!/bin/python3
import datetime
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QToolBar, QHBoxLayout
from PyQt6.QtCore import QSize, Qt
import sys
from Xlib import display, Xatom, X
from pygments.lexers.scripting import MiniScriptLexer
from screeninfo import get_monitors
from pynput import keyboard
from panel_widgets import MATButton, MiscButton, TimeWidget

# Subclass QMainWindow to customize your application's main window
class ArcaPanel(QWidget):
    def __init__(self, monitors):
        super().__init__()
        self._monitors = monitors
        self.main_monitor = monitors[0]

        # Initializes the variables
        self.layout = QHBoxLayout()
        self.mat_button = MATButton()
        self.misc_button = MiscButton("Logout")
        self.time_widget = TimeWidget()
        self.font = QFont()
        self.params = {}

        # Updates based on parameters in /etc/Arca/panel.conf
        self.update()

        # Sets the proper panel width
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setGeometry(0, 0, self.main_monitor.width, int(self.main_monitor.height * 0.05))  # Full width, thin

        # Sets the dimensions of the M.A.T. button
        self.mat_button.setFixedWidth(int(self.width() * 0.10))
        self.mat_button.setFixedHeight(int(self.height() * 0.5))

        # Sets the dimensions of the Misc button
        self.misc_button.setFixedWidth(int(self.width() * 0.10))
        self.misc_button.setFixedHeight(int(self.height() * 0.5))

        # Sets the dimensions of the Time widget
        self.time_widget.setFixedWidth(int(self.width() * 0.05))
        self.time_widget.setFixedHeight(int(self.height() * 0.5))

        # Sets the dimensions of the M.A.T. menu
        self.mat_button.mat_menu.setGeometry(0, self.height(), int(self.main_monitor.width * 0.25), int(self.main_monitor.height * 0.5))  # Full width, thin

        # Sets up the QHBoxLayout()
        self.layout.setSpacing(5)
        self.layout.addWidget(self.mat_button)
        self.layout.addWidget(self.misc_button)
        self.layout.addStretch()
        self.layout.addWidget(self.time_widget)
        self.setLayout(self.layout)

        # Starts time daemon
        self.time_widget.start()

        # Set strut to reserve panel space
        self.set_window_strut()

    def key_handler(self, key):
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys
        print(k)
        if k == 'cmd':
            self.mat_button.pressed()

    def set_window_strut(self):
        dpy = display.Display()
        xid = self.winId().__int__()  # Get X11 window ID
        window = dpy.create_resource_object('window', xid)
        # _NET_WM_STRUT_PARTIAL: [left, right, top, bottom, left_start_y, left_end_y, right_start_y, right_end_y, top_start_x, top_end_x, bottom_start_x, bottom_end_x]
        strut = [0, 0, self.height(), 0, 0, 0, 0, 0, 0, self.width(), 0, 0]  # Reserve 30px at top, across 0-1920px
        window.change_property(
            dpy.intern_atom('_NET_WM_STRUT_PARTIAL'),
            Xatom.CARDINAL, 32, strut, X.PropModeReplace
        )
        dpy.flush()
        dpy.close()

    def bind_func_to_misc_button(self, func):
        self.misc_button.set_func(func)

    def set_misc_button_text(self, text):
        self.misc_button.setText(text)

    def update(self):
        self._read_params()
        self._update_from_params()

    def _update_from_params(self):
        for param in self.params.keys():
            value = self.params[param]
            try:
                match param:
                    case 'PRIMARY_DISPLAY':
                        self.main_monitor = self._monitors[value]
                    case 'MISC_BUTTON_TEXT':
                        self.misc_button.setText(value)
                    case 'MISC_BUTTON_FUNC':
                        self.misc_button.set_func(value)
                    case 'FONT_SIZE':
                        self.font.setPointSize(value)
            except Exception as e:
                print(f"error parsing parameters from /etc/Arca/panel.conf: {e}")


    def _read_params(self):
        try:
            file = open('/etc/Arca/panel.conf', 'r')
        except FileNotFoundError as e:
            print("/etc/Arca/panel.conf not found... reverting to defaults")
            return
        for line in file:
            self.params[line.split('=', 1)[0]] = line.split('=', 1)[1]

    # Run this command BEFORE app.exec()
    def start(self):
        self.show()
        self.listener = keyboard.Listener(on_press=self.key_handler)
        self.listener.start()  # start to listen on a separate thread

    # Run this command AFTER app.exec()
    def stop(self):
        self.listener.join()  # remove if main thread is polling self.keys
        self.time_widget.stop()

def __main__():
    app = QApplication(sys.argv)
    monitors = get_monitors()
    window = ArcaPanel(monitors)
 	
	# Sets target user if specified
    if len(sys.argv) > 1:
        window.mat_button.mat_menu.user = sys.argv[1]

    # window.show()
    # listener = keyboard.Listener(on_press=window.key_handler)
    # listener.start()  # start to listen on a separate thread
    window.start()
    app.exec()
    # listener.join()  # remove if main thread is polling self.keys
    window.stop()

if __name__ == "__main__":
    __main__()
