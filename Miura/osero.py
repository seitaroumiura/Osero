# cSpell: ignore Miura Ishida numpy
import numpy as np
import Test


class Board():

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
    # 現在のボードの配列を返す
    def GetBoard(self):
        return self.field

    # Miura
    # 指定された場所に駒を置く
    # 置けなかったらエラーを出す
    def PutPiece(self, x, y):
        if(self.field[x][y] != self.EMPTY):
            raise RuntimeError("指定された場所に駒を置くことができません。")
        self.field[x][y] = self.turn

    # Miura
    # CUIで駒を表示します。
    def PrintBoard(self):
        CHAR_PEACE = [" ", "o", "*"]
        for i in self.field:
            print(end="|")
            for j in i:
                print(CHAR_PEACE[int(j)], end="|")
            print("\n------------------")

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
    Test.test_Board()
    Test.test_initBoard()
    Board().PrintBoard()
