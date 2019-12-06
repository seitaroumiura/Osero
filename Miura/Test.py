# cSpell: ignore numpy osero
# import numpy as np
from osero import Board


def test_Board():
    Board()
    print("OK:test_Board")


def test_initBoard():
    b = Board()
    b.initBoard()
    B = b.BLACK
    W = b.WHITE
    trueBoard = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, B, W, 0, 0, 0],
        [0, 0, 0, W, B, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    assert((b.field == trueBoard).all())
    print("OK:test_initBoard")


def test_SearchBoard():
    b = Board()
    B = b.BLACK
    W = b.WHITE
    b.field = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, B, W, 0, 0, 0],
        [0, 0, 0, B, W, 0, 0, 0],
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


def test_putPiece():
    b = Board()
    b.initBoard()
    b.PutPiece(2, 3)
    b.PrintBoard()