# cSpell: ignore numpy osero
# import numpy as np
from osero import Board


def test_Board():
    Board()
    print("OK:test_Board")


def test_initBoard():
    b = Board()
    b.initBoard()
    trueBoard = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 0, 0],
        [0, 0, 0, 1, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    assert((b.field == trueBoard).all())
    print("OK:test_initBoard")


def test_SearchBoard():
    b = Board()
    # TODO 色が逆になってる？
    # b.initBoard()
    res = b.SearchBoard(b.BLACK)
    b.PrintBoard()
    print(res)


def test_putPiece():
    b = Board()
    b.initBoard()
    b.PutPiece(2, 3)
    b.PrintBoard()