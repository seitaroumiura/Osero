import numpy as np
from Test import *

class  Board():
    
    # メンバ変数とフィールドの初期化
    def __init__(self):
        # メンバ変数の初期化
        self.field = np.zeros([8, 8])
        self.WHITE = 1
        self.BLACK = 2
        self.EMPTY = 0
        self.turn = self.BLACK

        # フィールドを初期化する
        self.field = np.zeros([8, 8])
        self.field[3, 3] = self.BLACK
        self.field[4, 4] = self.BLACK
        self.field[3, 4] = self.WHITE
        self.field[4, 3] = self.WHITE

    # 自身を初期化する
    def initBoard(self):
        self.__init__()

    # Miura
    def GetBoard(self):
        pass

    # Miura
    def PutPiece(self, x, y):
        pass

    # Miura
    def PrintBoard(self):
        pass

    # Ishida
    def SearchBoard(self):
        pass

    # Ishida
    def CheckBoard(self, x, y):
        pass

    # Ishida
    def CountPiece(self, color):
        pass

if __name__ == "__main__":
    test_Board()
    test_initBoard()