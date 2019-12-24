import sys
import pygame as pg
from pygame.locals import *
import numpy as np


class Board():
  # メンバ変数とフィールドの初期化
  def __init__(self):
    self.WHITE = 1
    self.BLACK = 2
    self.EMPTY = 0
    self.turn = self.BLACK

    self.field = np.full((8, 8), self.EMPTY)
    self.field[3, 3] = self.BLACK
    self.field[4, 4] = self.BLACK
    self.field[3, 4] = self.WHITE
    self.field[4, 3] = self.WHITE

  def initBoard(self):
    self.__init__()

  def GetBoard(self):
    return self.field

  def PutPiece(self, x, y):
    if not (np.array([[x, y]]) == self.SearchBoard(self.turn)).all(axis=1).any():
      print(self.SearchBoard(self.turn))
      raise RuntimeError("指定された場所に駒を置くことができません。")
    tmp = np.array([[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]])
    change = np.array([0, 0, 0, 0, 0, 0, 0, 0])
    check = np.array([0, 0, 0, 0, 0, 0, 0, 0])
    for i in range(8):
      for j in range(1, 8):
        if x + j * tmp[i][0] >= 0 and x + j * tmp[i][0] < 8 and y + j * tmp[i][1] >= 0 and y + j * tmp[i][1] < 8:
          if check[i] == 0:
            if self.field[x + j * tmp[i][0]][y + j * tmp[i][1]] == self.turn:
              if j != 1:
                check[i] = 1
                break
              else:
                check[i] = 2
                break
            elif self.field[x + j * tmp[i][0]][y + j * tmp[i][1]] == 0:
              check[i] = 2
              break
            else:
              change[i] += 1
      if check[i] == 1:
        for j in range(change[i] + 1):
          self.field[x + j * tmp[i][0]][y + j * tmp[i][1]] = self.turn

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

  def CheckBoard(self, x, y, color):
    if (np.array([[x, y]]) == self.SearchBoard(color)).all(axis=1).any():
      return True
    else:
      return False

  def CountPiece(self, color):
    return np.count_nonzero(self.field == color)

  # 引数
  # player1: None        人間の手で打つ
  #        : Playerクラス コンピュータ
  # player2: player1と同じ
  def run(self, player1=None, player2=None):
    SCREEN_X = 1040
    SCREEN_Y = 640
    CLOCK = pg.time.Clock()
    b = Board()
    pg.init()
    screen = pg.display.set_mode((SCREEN_X, SCREEN_Y))
    pg.display.set_caption("Osero")
    CLOCK.tick(60)

    # player1とplayer2の色を決める
    player_color = {
      b.BLACK: player1,
      b.WHITE: player2
    }
    
    while(1):
      screen.fill((255,255, 255))

      #draw1
      for i in range(8):
        for j in range(8):
          pg.draw.rect(screen, (0, 255, 0), Rect(200 + 80 * i, 80 * j, 80, 80))
          if b.field[i][j] == b.WHITE:
            pg.draw.circle(screen, (255, 255, 255), (240 + 80 * i, 40 + 80 * j), 30)
          elif b.field[i][j] == b.BLACK:
            pg.draw.circle(screen, (0, 0, 0), (240 + 80 * i, 40 + 80 * j), 30)
      #draw2
      for i in range(9):
        pg.draw.line(screen, (0, 0, 0), (200 + 80 * i, 0),(200 + 80 * i, SCREEN_Y), 4)
        pg.draw.line(screen, (0, 0, 0), (200, 80 * i),(SCREEN_X - 200, 80 * i), 4)
      #draw3
      font = pg.font.SysFont(None, 30)
      if b.turn == 1:
        text1 = font.render("Turn: White", True, (0, 0, 0))
      elif b.turn == 2:
        text1 = font.render("Turn: Black", True, (0, 0, 0))
      text2 = font.render("BLACK:" + str(b.CountPiece(b.BLACK)), True, (0, 0, 0))
      text3 = font.render("WHITE:" + str(b.CountPiece(b.WHITE)), True, (0, 0, 0))

      screen.blit(text1, (50, 100))
      screen.blit(text2, (900, 100))
      screen.blit(text3, (900, 150))
      #Update screen
      pg.display.update()
    
      #quit/command
      for event in pg.event.get():
        if event.type == QUIT:
          pg.quit()
          sys.exit()
        if event.type == MOUSEBUTTONDOWN and event.button == 1 or player_color[b.turn] is not None:

          # 人間の番    
          if player_color[b.turn] is None:
            x, y = event.pos
            sx = (x - 200) // 80
            sy = y // 80
          else:
            sx, sy = player_color[b.turn].get_position(b.GetBoard())

          print("----------")
          print(b.CheckBoard(sx, sy, b.turn))
          print(np.array([[sx, sy]]))
          print('\n')
          print(b.SearchBoard(b.turn))
          print("----------")
          if b.CheckBoard(sx, sy, b.turn):
            b.PutPiece(sx, sy)
            if b.turn == b.WHITE:
              b.turn = b.BLACK
            else:
              b.turn = b.WHITE


if __name__ == "__main__":
  b = Board()
  b.run()
