import sys
from PyQt5.QtWidgets import QApplication,QWidget, QLabel, QPushButton
from PyQt5 import QtGui
import random


class MainWindow(QWidget):
    life = 5 #맞추면 +1 틀리면 -1
    target = 0 #난이도에 따라 6 8 10으로 설정됨.
    turn = 0 #턴이 진행될 때마다 1씩 증가
    draw_card = {'Color':'', 'Number':''}
    player_cards = []
    black_card = [i for i in range(0, 12)]
    white_card = [i for i in range(0, 12)]

    def setLife(self, life):
        self.life = life

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lifeLabel = QLabel("목숨 :", self)
        self.lifeLabelValue = QLabel(str(self.life), self)
        self.turnLabel = QLabel("라운드 :", self)
        self.turnLabelValue = QLabel(str(self.turn), self)

        self.lifeLabel.move(400, 600)
        self.lifeLabelValue.move(480, 600)
        self.turnLabel.move(700, 600)
        self.turnLabelValue.move(800, 600)
        self.lifeLabel.setFont(QtGui.QFont("궁서", 20))
        self.lifeLabelValue.setFont(QtGui.QFont("궁서", 20))
        self.turnLabel.setFont(QtGui.QFont("궁서", 20))
        self.turnLabelValue.setFont(QtGui.QFont("궁서", 20))

        self.setWindowTitle("나를 맞춰봐!")
        self.setGeometry(250, 0, 1500, 1000)
        self.show()

    def cardDraw(self): # 카드 뽑기
        # 검은 카드를 선택한 경우
        self.draw_card['Color'] = 'black'
        self.draw_card['Number'] = random.choice(self.black_card)
        self.black_card.remove(self.draw_card['Number'])
        # 흰 카드를 선택한 경우
        self.draw_card['Color'] = 'white'
        self.draw_card['Number'] = random.choice(self.white_card)
        self.white_card.remove(self.draw_card['Number'])

        # 플레이어 패에 적용
        self.player_cards.append(self.draw_card)

    def cardSort(self): # 카드 정렬
        pass




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())