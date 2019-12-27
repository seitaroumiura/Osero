class Player:

    def __init__(self):
        raise(RuntimeError("__init__メソッドが定義されていません。"))

    # 引数
    # board: Boardクラスのコピーを受けとる。 
    # 戻り値
    # [x, y]
    def get_position(self, board):
        raise(RuntimeError("get_positionメソッドが定義されていません。"))