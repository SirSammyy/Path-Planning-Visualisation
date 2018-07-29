import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMainWindow
from PyQt5.QtGui import QIcon

class PPVMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Test")
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage("Status Bar")
        self.initUI()

    def initUI(self):
        print("Window Made")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ppv = PPVMainWindow()
    ppv.show()
    sys.exit(app.exec())
