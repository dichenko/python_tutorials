import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Первая программа')

        self.btn = QPushButton('Кнопка', self)
        self.btn.resize(150, 100)
        self.btn.move(75, 150)

        self.btn.clicked.connect(self.hello)

    def hello(self):
        self.btn.setText('Привет')


app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())
