import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QLineEdit,
                             QHBoxLayout, QVBoxLayout, QApplication)


class GetCard(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # hbox
        self.hbox = QHBoxLayout()
        self.index = QLabel("카드 위치 :")
        self.indexEdit = QLineEdit()
        self.number = QLabel("예상 숫자 :")
        self.numberEdit = QLineEdit()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.index)
        self.hbox.addWidget(self.indexEdit)
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.number)
        self.hbox.addWidget(self.numberEdit)
        self.hbox.addStretch(1)

        # hbox2
        self.hbox2 = QHBoxLayout()
        self.checkButton = QPushButton("입력", self)
        self.hbox2.addStretch(1)
        self.hbox2.addWidget(self.checkButton)
        self.hbox2.addStretch(1)

        # vbox
        self.vbox = QVBoxLayout()
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addStretch(1)

        self.setLayout(self.vbox)

        self.setWindowTitle('상대방 패 맞추기')
        self.setGeometry(750, 450, 500, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    getC = GetCard()
    sys.exit(app.exec_())


