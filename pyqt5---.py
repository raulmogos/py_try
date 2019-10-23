import sys

from PyQt5.QtWidgets import QApplication, QWidget


def run():
    app = QApplication(sys.argv)

    start = QWidget()
    start.show()

    sys.exit(app.exec_())

run()
