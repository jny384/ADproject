import sys
import GetCard
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)

"""

"""

class Difficulty(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.easyButton = QPushButton("쉬움", self)
        self.normalButton = QPushButton("보통", self)
        self.hardButton = QPushButton("어려움", self)

        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.easyButton)
        self.hbox.addWidget(self.normalButton)
        self.hbox.addWidget(self.hardButton)
        self.hbox.addStretch(1)

        self.vbox = QVBoxLayout()
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox)
        self.vbox.addStretch(1)

        self.setLayout(self.vbox)

        self.setWindowTitle('난이도를 선택하세요')
        self.setGeometry(800, 450, 300, 200)
        self.show()

        self.easyButton.clicked.connect(self.clickEasy)
        self.normalButton.clicked.connect(self.clickNormal)
        self.hardButton.clicked.connect(self.clickHard)

    def clickEasy(self):
        #Difficult GUI 종료하고, 쉬움을 인자로 하는 메인화면으로,
        self.dif = GetCard.GetCard()

        pass

    def clickNormal(self):
        # Difficult GUI 종료하고, 통을 인자로 하는 메인화면으로,
        pass

    def clickHard(self):
        # Difficult GUI 종료하고, 어려움을 인자로 하는 메인화면으로,
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dif = Difficulty()
    sys.exit(app.exec_())

