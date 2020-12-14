import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui


import random

target = 0  # 맞추면 +1 틀리면 -1
class GameStart(QWidget):
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
        global target
        target = 6
        self.mainWindow = MainWindow()
        self.dif_dialog_close()

    def clickNormal(self):
        # Difficult GUI 종료하고, 통을 인자로 하는 메인화면으로,
        global target
        target = 8
        self.mainWindow = MainWindow()
        self.dif_dialog_close()

    def clickHard(self):
        # Difficult GUI 종료하고, 어려움을 인자로 하는 메인화면으로,
        global target
        target = 10
        self.mainWindow = MainWindow()
        self.dif_dialog_close()

class MainWindow(QWidget):
    life = 5 #플레이어의 목숨.
    turn = 1 #턴이 진행될 때마다 1씩 증가

    player_cards = [] #플레이어가 가지고 있는 카드. Draw 할때마다 인자의 정수 값만큼 증가
    computer_cards = [] #컴퓨터가 가지고 있는 카드. target값과 같음.
    black_card = [i for i in range(0, 12)] # 0부터 11까지의 숫자로 구성된 검은 패. Draw 할 때마다 감소함.
    white_card = [i for i in range(0, 12)] # 0부터 11까지의 숫자로 구성된 흰 패. Draw 할 때마다 감소함.
    computerCardDic = {} # 패를 맞추기 위해 만들어진 딕셔너리
    complete_check = [] # 이미 맞춘 컴퓨터의 패를 식별하기 위해 만들어진 리스트
    check_info = "" # buttonClicked에서 쓰이는, 컴퓨터의 패를 맞출 때 활용되는 변수.

    def __init__(self):
        super().__init__()
        self.initUI()
        self.cardDraw("computer", target, "")
        self.cardDraw("player", 4, "")
        self.cardSort("computer")
        self.cardSort("player")
        self.playerCardDraw()

    def initUI(self):
        self.textLayout = QGridLayout()
        self.drawLayout = QGridLayout()
        self.playerCardLayout = QGridLayout()
        self.mainLayout = QGridLayout()


        lifeLabel = QLabel("목숨 :", self)
        self.lifeLabelValue = QLabel(str(self.life), self)
        turnLabel = QLabel("라운드 :", self)
        self.turnLabelValue = QLabel(str(self.turn), self)

        lifeLabel.setFont(QtGui.QFont("궁서", 20))
        self.lifeLabelValue.setFont(QtGui.QFont("궁서", 20))
        turnLabel.setFont(QtGui.QFont("궁서", 20))
        self.turnLabelValue.setFont(QtGui.QFont("궁서", 20))

        self.textLayout.addWidget(lifeLabel, 0, 0)
        self.textLayout.addWidget(self.lifeLabelValue, 0, 1)
        self.textLayout.addWidget(turnLabel, 0, 2)
        self.textLayout.addWidget(self.turnLabelValue, 0, 3)
        self.mainLayout.addLayout(self.textLayout, 2, 0)
        self.setWindowTitle("나를 맞춰봐!")
        self.setGeometry(250, 0, 1500, 1000)
        self.show()
        self.setLayout(self.mainLayout)

    def mainGame(self):
        while(self.life > 0 or target > 0):
            self.cardDraw("player", 1)
            self.cardSort("player")
            #카드 맞추고
            #맞춘카드 보이게하고
            #재도전 가능하고(틀리거나 그만할때까지) (틀리면 self.life -= 1)
            #turn += 1
            pass

    def cardDraw(self, object, target, color): # 카드 뽑기
        count = target
        draw_card = {'Color':'', 'Number':''}
        while(count > 0):
            if color == "":
                black_white = random.randrange(0, 2)
            else:
                black_white = color

            if black_white == 0 or black_white == "black":
                draw_card['Color'] = 'black'
                draw_card['Number'] = random.choice(self.black_card)
                self.black_card.remove(draw_card['Number'])
                count -= 1

            elif black_white == 1 or black_white == "white":
                draw_card['Color'] = 'white'
                draw_card['Number'] = random.choice(self.white_card)
                self.white_card.remove(draw_card['Number'])
                count -= 1

            if object == "computer":
                self.computer_cards.append({'Color':draw_card['Color'], 'Number':draw_card['Number']})
            elif object == "player":
                self.player_cards.append({'Color': draw_card['Color'], 'Number': draw_card['Number']})

    def cardSort(self, object): # 카드 정렬한 후 GUI로 표현

        self.mainLayout.removeItem(self.playerCardLayout)
        self.computerCardLayout = QGridLayout()

        object_key = {"computer" : 0, "player" : 1}
        cards_key = [self.computer_cards, self.player_cards]
        layout_key = [self.computerCardLayout, self.playerCardLayout]
        index = [0, 4]

        # 숫자를 기준으로 정렬
        btnList = []
        for card in sorted(cards_key[object_key[object]], key=lambda draw_card: draw_card['Number']):
            btnList.append(card)

        # 카드 색을 기준으로 정렬
        tmp = btnList[0]
        for i in range(1, len(btnList)):
            if tmp['Number'] == btnList[i]['Number'] and tmp['Color'] == 'white':
                a = btnList[i]
                btnList[i] = tmp
                btnList[i-1] = a
            else:
                tmp = btnList[i]

        # 정렬이 완료된 패를 GUI로 구현
        c = 0
        i = 0
        for btn in btnList:
            cardButton = Button(btn['Color'] + "\n" + str(btn['Number']), self.buttonClicked)
            # QDialog 설정
            self.check_dialog = QDialog()

            if btn['Color'] == 'black':
                cardButton.setStyleSheet('color:white;background:black')
                if cardButton.text() in self.complete_check:
                    cardButton.setStyleSheet('color:rgba(255, 255, 255, 100%);background:black')
                    i += 1
                elif object == "computer":
                    cardButton.setStyleSheet('color:rgba(255, 255, 255, 0%);background:black')
                    self.computerCardDic[i] = btn['Color'] + "\n" + str(btn['Number'])
                    i += 1
            else:
                cardButton.setStyleSheet('color:black;background:white')
                if cardButton.text() in self.complete_check:
                    cardButton.setStyleSheet('color:rgba(0, 0, 0, 100%);background:white')
                    i += 1
                elif object == "computer":
                    cardButton.setStyleSheet('color:rgba(0, 0, 0, 0%);background:white')
                    self.computerCardDic[f'{i}'] = btn['Color'] + "\n" + str(btn['Number'])
                    i += 1

            cardButton.setMaximumHeight(170)
            cardButton.setMaximumWidth(100)
            cardButton.setFont(QtGui.QFont("궁서", 15))

            layout_key[object_key[object]].addWidget(cardButton, 0, c)
            c += 1

        self.mainLayout.addLayout(layout_key[object_key[object]], index[object_key[object]], 0)
        self.setLayout(self.mainLayout)

    def playerCardDraw(self): # 플레이어 카드뽑기 칸
        whiteDrawButton = Button(("white\nCard\nDraw"), self.buttonClicked)
        blackDrawButton = Button(("black\nCard\nDraw"), self.buttonClicked)
        whiteDrawButton.setFont(QtGui.QFont("궁서", 10))
        blackDrawButton.setFont(QtGui.QFont("궁서", 10))
        whiteDrawButton.setMaximumHeight(170)
        whiteDrawButton.setMaximumWidth(100)
        blackDrawButton.setMaximumHeight(170)
        blackDrawButton.setMaximumWidth(100)
        self.drawLayout.addWidget(whiteDrawButton, 0, 0, 2, 1)
        self.drawLayout.addWidget(blackDrawButton, 0, 1, 2, 1)
        self.mainLayout.addLayout(self.drawLayout, 1, 0)

    def buttonClicked(self):
        button = self.sender()
        key = button.text()

        self.againAndEnd_dialog = QDialog()
        self.gameEnd_dialog = QDialog()
        s = setting()

        if key in self.computerCardDic.values():
            self.check_info = key
            self.check_open()

        elif key == "Send":
            if self.checkText.text() == self.check_info.replace("white","").replace("black","").replace("\n",""):
                self.againAndEnd_dialog = QDialog()
                self.complete_check.append(self.check_info)
                self.cardSort("computer")
                self.check_dialog.close()
                self.againAndEnd_open()
                s.subTarget(1)
            else:
                self.false_dialog = QDialog()
                self.false_open()

        elif key == "Ok":
            self.false_dialog.close()
            self.check_dialog.close()
            self.life-=1
            self.turn+=1
            self.lifeLabelValue.setText(str(self.life))
            self.turnLabelValue.setText(str(self.turn))

        elif key == "Cancel":
            self.check_dialog.close()

        elif key == "Again":
            self.againAndEnd_dialog.close()
            self.check_dialog.close()

        elif key == "End":
            self.againAndEnd_dialog.close()
            self.check_dialog.close()
            self.turn += 1
            self.turnLabelValue.setText(str(self.turn))

        elif key == "white\nCard\nDraw":
            if len(self.white_card)>0:
                self.cardDraw("player", 1, "white")
                self.cardSort("player")
            else:
                pass

        elif key == "black\nCard\nDraw":
            if len(self.black_card) > 0:
                self.cardDraw("player", 1, "black")
                self.cardSort("player")
            else:
                pass

        elif key == "Game End":
            sys.exit()

        if target == 0:
            self.gameEnd_open("win")

        elif self.life == 0:
            self.gameEnd_open("lose")

    def check_open(self):
        self.checkText = QLineEdit("", self.check_dialog)

        sendButton = QPushButton("Send", self.check_dialog)
        cancelButton = QPushButton("Cancel", self.check_dialog)

        sendButton.clicked.connect(self.buttonClicked)
        cancelButton.clicked.connect(self.buttonClicked)

        self.checkText.move(100, 35)
        sendButton.setGeometry(120, 85, 60, 30)
        cancelButton.setGeometry(120, 135, 60, 30)

        # QDialog 세팅
        self.check_dialog.setWindowTitle('패 맞추기')
        self.check_dialog.setWindowModality(Qt.ApplicationModal)
        self.check_dialog.resize(300, 200)
        self.check_dialog.show()

    def againAndEnd_open(self):
        againButton = QPushButton("Again", self.againAndEnd_dialog)
        endButton = QPushButton("End", self.againAndEnd_dialog)

        againButton.clicked.connect(self.buttonClicked)
        endButton.clicked.connect(self.buttonClicked)

        againButton.setGeometry(120, 85, 60, 30)
        endButton.setGeometry(120, 135, 60, 30)

        # QDialog 세팅
        self.againAndEnd_dialog.setWindowTitle('한 번 더 맞추기')
        self.againAndEnd_dialog.setWindowModality(Qt.ApplicationModal)
        self.againAndEnd_dialog.resize(300, 185)
        self.againAndEnd_dialog.show()

    def false_open(self):
        okButton = QPushButton("Ok", self.false_dialog)

        okButton.clicked.connect(self.buttonClicked)

        okButton.setGeometry(120, 85, 60, 30)

        # QDialog 세팅
        self.false_dialog.setWindowTitle('틀렸습니다!')
        self.false_dialog.setWindowModality(Qt.ApplicationModal)
        self.false_dialog.resize(300, 185)
        self.false_dialog.show()

    def gameEnd_open(self, state):
        gameEndButton = QPushButton("Game End", self.gameEnd_dialog)
        if state == "lose":
            stateLabel = QLabel("Game Over", self.gameEnd_dialog)
            stateLabel.setStyleSheet('color:rgba(255, 0, 0, 100%);')
            self.gameEnd_dialog.setWindowTitle('패')

        elif state == "win":
            stateLabel = QLabel("Victory!", self.gameEnd_dialog)
            stateLabel.setStyleSheet('color:rgba(0, 0, 255, 100%);')
            self.gameEnd_dialog.setWindowTitle('승리')

        stateLabel.setFont(QtGui.QFont("궁서", 20))
        gameEndButton.clicked.connect(self.buttonClicked)
        stateLabel.move(90, 45)
        gameEndButton.setGeometry(120, 85, 60, 30)

        # QDialog 세팅
        self.gameEnd_dialog.setWindowModality(Qt.ApplicationModal)
        self.gameEnd_dialog.resize(300, 185)
        self.gameEnd_dialog.show()

class Button(QToolButton):
    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size

class setting():
    def subTarget(self, i):
        global target
        a = target
        target = a - i

app = QApplication(sys.argv)
gameStart = GameStart()
sys.exit(app.exec_())
