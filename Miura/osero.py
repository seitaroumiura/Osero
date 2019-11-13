import numpy as np
from Test import *

class  Board():
    
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

    def initBoard(self):
        self.__init__()

    def GetBoard(self):
        pass

    def PutPiece(self, x, y):
        pass

    def PrintBoard(self):
        pass

    def SearchBoard(self):
        pass

    def CheckBoard(self, x, y):
        pass

    def CountPiece(self, color):
        pass

if __name__ == "__main__":
    test_Board()
    test_initBoard()