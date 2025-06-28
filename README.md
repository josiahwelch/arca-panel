# arca-panel
Top panel designed for the Arca Desktop Manager

No one is going to read this readme...

## Usage
Normally, the Arca panel shouldn't be used outside the Arca DM. However, if you were brave enough to use the Arca Panel out of the box, here would be the code snippet to get it to work:

```
app = QApplication(sys.argv)
monitors = get_monitors()
window = ArcaPanel(monitors)
window.start()
app.exec()
window.stop()
```

Here is a breakdown of what is happening...

`app = QApplication(sys.argv)`: creates the QT application

`monitors = get_monitors()`: prevents the wrong monitor to be targeted in a multi-monitor setup

`window = ArcaPanel(monitors)`: creates the instance of the ArcaPanel class

`window.start()`: starts the Arca panel

`app.exec()`: starts the QT application

`window.stop()`: stops the Arca panel after application execution is completed or halted

## Dependencies

I am probably missing a few, based on what platform is being targeted.

- Python 3.10+
  - desktop-parser 0.1.1
  - Pygments 2.17.2
  - PyQT6 6.6.1
