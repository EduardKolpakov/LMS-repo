import sys

import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor


class yellow_circles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.qp = QPainter()
        self.flag = False
        self.add.clicked.connect(self.drawf)

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        self.qp.setBrush(QColor(255, 255, 0))
        x = random.randint(1, 75)
        self.qp.drawEllipse(random.randint(0, 1404), random.randint(0, 927), x, x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = yellow_circles()
    ex.show()
    sys.exit(app.exec_())
