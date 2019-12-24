from Player import Player
import random

# 打てる手のなかからランダムに手を選択する
class random_player(Player):

    def __init__(self):
        pass

    def get_position(self, board):
        can_position = board.SearchBoard(board.turn)
        return can_position[random.randint(0, len(can_position) - 1)]
