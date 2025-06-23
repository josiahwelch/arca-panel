def remove_widgets(layout):
    for i in reversed(range(layout.count())):
        layout.itemAt(i).widget().setParent(None)