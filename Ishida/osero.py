# cSpell: ignore Miura Ishida numpy
import copy
import numpy as np

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
        # 駒を置けるかを確認
        if not [x, y] in self.SearchBoard(self.turn):
            print(self.SearchBoard(self.turn))
            raise RuntimeError("指定された場所に駒を置くことができません。")
        # self.turn = self.WHITE
        self.field[x][y] = self.turn

        # 裏返しにする方向の決定
        directions = [
            [1, 0], [-1, 0], [0, 1], [0, -1],
            [1, 1], [-1, 1], [1, -1], [-1, -1]
        ]
        for d in directions:
            pos_x = x
            pos_y = y
            # *pythonには浅いコピーと深いコピーがある
            # *浅いコピーでは、コピー元のデータが書き変えられると
            # *コピー先の内容も変わってしまう。
            # *https://techblog.recochoku.jp/515
            copyBoard = copy.deepcopy(self.field)
            while(True):
                print("ok")
                pos_x += d[0]
                pos_y += d[1]

                # 端まで行ったらループを終了
                if not (0 < pos_x < 8 or 0 < pos_y < 8):
                    print(1)
                    self.field = copyBoard
                    break
                if self.field[pos_x][pos_y] != self.turn and self.field[pos_x][pos_y] != self.EMPTY:  # 相手の駒があった場合
                    self.field[pos_x][pos_y] = self.turn
                if self.field[pos_x][pos_y] == self.EMPTY:
                    self.field = copyBoard
                    break
                if self.field[pos_x][pos_y] == self.turn:
                    break

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
    # return: [y, x]
    def SearchBoard(self, color):
        c_list = np.empty((0, 2), int)
        result = np.empty((0, 2), int)
        check = np.array([0, 0, 0, 0, 0, 0, 0, 0])
        tmp = np.array([[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]])
        for i in range(8):
            for j in range(8):
                if self.field[i][j] == 0:
                    c_list = np.append(c_list, np.array([[i, j]]), axis = 0)
        for i in range(c_list.shape[0]):
            check = np.array([0, 0, 0, 0, 0, 0, 0, 0])
            for j in range(1, 8):
                for k in range(8):
                    if c_list[i][0] + j * tmp[k][0] >= 0 and c_list[i][0] + j * tmp[k][0] < 8 and c_list[i][1] + j * tmp[k][1] >= 0 and c_list[i][1] + j * tmp[k][1] < 8:
                        if check[k] == 0:
                            if self.field[c_list[i][0] + j * tmp[k][0]][c_list[i][1] + j * tmp[k][1]] == color:
                                if j != 1:
                                    check[k] = 1
                                else:
                                    check[k] = 2
                            elif self.field[c_list[i][0] + j * tmp[k][0]][c_list[i][1] + j * tmp[k][1]] == 0:
                                check[k] = 2
                            else:
                                pass
            if 1 in check:
                result = np.append(result, np.array([c_list[i]]), axis = 0)
        return result

    # Ishida
    def CheckBoard(self, x, y, color):
        tmp = self.SearchBoard(color)
        if [x, y] in tmp:
            return True

    # Ishida
    def CountPiece(self, color):
        return np.count_nonzero(self.field == color)


if __name__ == "__main__":
    b = Board()
    B = b.BLACK
    W = b.WHITE
    b.field = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, B, W, 0, 0, 0],
        [0, 0, 0, W, B, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    print("BLACK")
    res = b.SearchBoard(b.BLACK)
    b.PrintBoard()
    print(res)
    
    print("\nWHITE")
    res = b.SearchBoard(b.WHITE)
    b.PrintBoard()
    print(res)

    # ### 疑問点
    # 置ける場所の内、左横が見落とされている？
    # ### 実行結果
    #   BLACK
    #   | | | | | | | | |
    #   ------------------
    #   | | | | | | | | |
    #   ------------------
    #   | | | | | | | | |
    #   ------------------
    #   | | | |*|o| | | |
    #   ------------------
    #   | | | |*|o| | | |
    #   ------------------
    #   | | | | | | | | |
    #   ------------------
    #   | | | | | | | | |
    #   ------------------
    #   | | | | | | | | |
    #   ------------------
    #   [[2 2]
    #    [3 2]]

    #   WHITE
    #   | | | | | | | | |
    #   ------------------
    #   | | | | | | | | |
    #   ------------------
    #   | | | | | | | | |
    #   ------------------
    #   | | | |*|o| | | |
    #   ------------------
    #   | | | |*|o| | | |
    #   ------------------
    #   | | | | | | | | |
    #   ------------------
    #   | | | | | | | | |
    #   ------------------
    #   | | | | | | | | |
    #   ------------------
    #   [[2 5]
    #    [3 5]]
