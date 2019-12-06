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
    def GetBoard(self):
        pass

    # Miura
    def PutPiece(self, x, y):
        pass

    # Miura
    def PrintBoard(self):
        pass

    # Ishida
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
            for j in range(2, 8):
                for k in range(8):
                    if c_list[i][0] + j * tmp[k][0] >= 0 and c_list[i][0] + j * tmp[k][0] < 8 and c_list[i][1] + j * tmp[k][1] >= 0 and c_list[i][1] + j * tmp[k][1] < 8:
                        if self.field[c_list[i][0] + tmp[k][0]][c_list[i][1] + tmp[k][1]] == color and check[k] != 2:
                            if self.field[c_list[i][0] + j * tmp[k][0]][c_list[i][1] + j * tmp[k][1]] == color:
                                pass
                            elif self.field[c_list[i][0] + j * tmp[k][0]][c_list[i][1] + j * tmp[k][1]] == self.EMPTY:
                                check[k] = 2
                            else:
                                check[k] = 1
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
    Test = Board()
    print(Test.SearchBoard(Test.WHITE))