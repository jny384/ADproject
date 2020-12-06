import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import GameMain

class GameStart(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.startButton = QPushButton("게임실행", self)
        self.exitButton = QPushButton("게임종료", self)

        # QButton 위젯 생성
        self.startButton.clicked.connect(self.difficulty_open)
        self.startButton.setGeometry(120, 45, 60, 30)
        self.exitButton.clicked.connect(self.gameExit)
        self.exitButton.setGeometry(120, 95, 60, 30)

        # QDialog 설정
        self.dif_dialog = QDialog()

        self.setGeometry(833, 440, 300, 170)  # x, y, w, h
        self.setWindowTitle("나를 맞춰봐!")
        self.show()

    def gameExit(self):
        sys.exit()

    def difficulty_open(self):
        # 버튼 추가
        self.easyButton = QPushButton('쉬움', self.dif_dialog)
        self.normalButton = QPushButton("보통", self.dif_dialog)
        self.hardButton = QPushButton("어려움", self.dif_dialog)

        self.easyButton.setGeometry(120, 35, 60, 30)
        self.normalButton.setGeometry(120, 85, 60, 30)
        self.hardButton.setGeometry(120, 135, 60, 30)

        self.easyButton.clicked.connect(self.clickEasy)
        self.normalButton.clicked.connect(self.clickNormal)
        self.hardButton.clicked.connect(self.clickHard)

        # QDialog 세팅
        self.dif_dialog.setWindowTitle('난이도 선택')
        self.dif_dialog.setWindowModality(Qt.ApplicationModal)
        self.dif_dialog.resize(300, 200)
        self.dif_dialog.show()

    def dif_dialog_close(self):
        self.dif_dialog.close()

    def clickEasy(self):
        # Difficult GUI 종료하고, 쉬움을 인자로 하는 메인화면으로,
        self.mainWindow = GameMain.MainWindow()
        GameMain.MainWindow.target = 6 # 다양한 시도
        self.dif_dialog_close()


    def clickNormal(self):
        # Difficult GUI 종료하고, 통을 인자로 하는 메인화면으로,
        self.mainWindow = GameMain.MainWindow()
        self.mainWindow.setLife(8) # 다양한 시도 ㅎㅎ
        self.dif_dialog_close()


    def clickHard(self):
        # Difficult GUI 종료하고, 어려움을 인자로 하는 메인화면으로,
        self.mainWindow = GameMain.MainWindow()
        GameMain.MainWindow.target = 10
        self.dif_dialog_close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gameStart = GameStart()
    sys.exit(app.exec_())