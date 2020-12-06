class Hangman:

    text = [

'''\
 _____________
|    black    |
|             |
|             |
|             |
|             |
|             |
|_____________|\
''',

'''\
 _____________
|    white    |
|             |
|             |
|             |
|             |
|             |
|_____________|\
'''
    ]


    def __init__(self):
        self.remainingLives = len(self.text) - 1


    def decreaseLife(self):
        self.remainingLives -= 1


    def currentShape(self):
        return self.text[self.remainingLives]

