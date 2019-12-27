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
    tmp = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    change = [0, 0, 0, 0, 0, 0, 0, 0]
    check = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
      for j in range(1, 8):
        dx = j * tmp[i][0]
        dy = j * tmp[i][1]
        if x + dx >= 0 and x + dx < 8 and y + dy >= 0 and y + dy < 8:
          if check[i] == 0:
            if self.field[x + dx][y + dy] == self.turn:
              if j != 1:
                check[i] = 1
                break
              else:
                check[i] = 2
                break
            elif self.field[x + dx][y + dy] == 0:
              check[i] = 2
              break
            else:
              change[i] += 1
      if check[i] == 1:
        for j in range(change[i] + 1):
          self.field[x + j * tmp[i][0]][y + j * tmp[i][1]] = self.turn

  def SearchBoard(self, color):
    c_list = []
    result = []
    check = [0, 0, 0, 0, 0, 0, 0, 0]
    tmp = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for i in range(8):
      for j in range(8):
        if self.field[i][j] == 0:
          c_list.append([i, j])
    for i in range(len(c_list)):
      check = [0, 0, 0, 0, 0, 0, 0, 0]
      for j in range(1, 8):
        for k in range(8):
          sx = c_list[i][0] + j * tmp[k][0]
          sy = c_list[i][1] + j * tmp[k][1]
          if sx >= 0 and sx < 8 and sy >= 0 and sy < 8:
            if check[k] == 0:
              if self.field[sx][sy] == color:
                if j != 1:
                  check[k] = 1
                else:
                  check[k] = 2
              elif self.field[sx][sy] == 0:
                check[k] = 2
              else:
                pass
      if 1 in check:
        result.append(c_list[i])
    return np.array(result)

  def CheckBoard(self, x, y, color):
    if (np.array([[x, y]]) == self.SearchBoard(color)).all(axis=1).any():
      return True
    else:
      return False

  def CountPiece(self, color):
    return np.count_nonzero(self.field == color)

class MonteCarlo():
  def __init__(self, color, depth, repeat):
    self.color = color
    self.Depth = depth
    self.Repeat = repeat
    self.Selected = []
    self.Selected_NUM = []
    self.Score = []

  def Select(self, board):
    self.Selected_NUM = []
    self.Selected = [deepcopy(board)]
    for i in range(self.Depth):
      NextSelect = []
      NextSelect_NUM = []
      for j in range(len(self.Selected)):
        lst = self.Selected[j].SearchBoard(self.Selected[j].turn)
        for k in range(lst.shape[0]):
          NextBoard = deepcopy(self.Selected[j])
          NextBoard.PutPiece(lst[k][0], lst[k][1])
          NextSelect.append(deepcopy(NextBoard))
          if i == 0:
            NextSelect_NUM.append(k)
          else:
            NextSelect_NUM.append(self.Selected_NUM[j])
      self.Selected = NextSelect
      self.Selected_NUM = NextSelect_NUM

  def Expand(self):
    self.Score = []
    for i in range(len(self.Selected)):
      win = 0
      t1 = time.time()
      for j in range(self.Repeat):
        #Copy Expand Board
        Run = deepcopy(self.Selected[i])
        #Expand
        while True:
          lst = Run.SearchBoard(Run.turn)
          P_B = Run.CountPiece(Run.BLACK)
          P_W = Run.CountPiece(Run.WHITE)
          #Choice & Put Piece
          if lst.shape[0] != 0:
            choice = np.random.randint(lst.shape[0])
            Run.PutPiece(lst[choice][0], lst[choice][1])
            if Run.turn == Run.WHITE:
              Run.turn = Run.BLACK
            else:
              Run.turn = Run.WHITE
          else:
            #End Game(1)
            if Run.SearchBoard(Run.BLACK).shape[0] == 0 and Run.SearchBoard(Run.WHITE).shape[0] == 0:
              if P_B > P_W and self.color == Run.BLACK:
                win += 1
              elif P_W > P_B and self.color == Run.WHITE:
                win += 1
              break
            #Skip turn
            else:
              if Run.turn == Run.WHITE:
                Run.turn = Run.BLACK
              else:
                Run.turn = Run.WHITE
      t2 = time.time()
      elapsed_time = t2 - t1
      print(f"<Debug>\n処理時間:{elapsed_time}")
      print(win)
      self.Score.append(win / self.Repeat)
  
  def Choice(self):
    score_max = 0
    choice = 0
    for i in range(len(self.Score)):
      if score_max < self.Score[i]:
        score_max = self.Score[i]
        choice = self.Selected_NUM[i]
    return choice


def main():
  SCREEN_X = 1040
  SCREEN_Y = 640
  CLOCK = pg.time.Clock()
  b = Board()
  AI1 = MonteCarlo(b.WHITE, 1, 100)
  AI2 = MonteCarlo(b.BLACK, 1, 200)
  pg.init()
  screen = pg.display.set_mode((SCREEN_X, SCREEN_Y))
  pg.display.set_caption("Osero")
  CLOCK.tick(60)
  while(1):
    #Fill screen 
    screen.fill((255,255, 255))

    #Check "End the Game"
    if b.CountPiece(b.BLACK) + b.CountPiece(b.WHITE) == 64 or b.CountPiece(b.BLACK) == 0 or b.CountPiece(b.WHITE) == 0:
      print("BRACK:" + str(b.CountPiece(b.BLACK)) + "\nWHITE:" + str(b.CountPiece(b.WHITE)))
      pg.quit()
      sys.exit()
    if b.SearchBoard(b.BLACK).shape[0] == 0 and b.SearchBoard(b.WHITE).shape[0] == 0:
      print("BRACK:" + str(b.CountPiece(b.BLACK)) + "\nWHITE:" + str(b.CountPiece(b.WHITE)))
      pg.quit()
      sys.exit()

    #Check "Skip turn?"
    if b.SearchBoard(b.turn).shape[0] == 0:
      if b.turn == b.WHITE:
        b.turn = b.BLACK
      else:
        b.turn = b.WHITE

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
      text1 = font.render("Turn: Brack", True, (0, 0, 0))
    text2 = font.render("BRACK:" + str(b.CountPiece(b.BLACK)), True, (0, 0, 0))
    text3 = font.render("WHITE:" + str(b.CountPiece(b.WHITE)), True, (0, 0, 0))
    screen.blit(text1, (50, 100))
    screen.blit(text2, (900, 100))
    screen.blit(text3, (900, 150))

    #Update screen
    pg.display.update()

    # MonteCarlo's Turn
    if b.turn == AI1.color:
      AI1.Select(b)
      AI1.Expand()
      num = AI1.Choice()
      #print(num)
      sx = b.SearchBoard(b.turn)[num][0]
      sy = b.SearchBoard(b.turn)[num][1]
      #print([sx, sy])
      #print(b.SearchBoard(b.turn))
      b.PutPiece(sx, sy)
      if b.turn == b.WHITE:
        b.turn = b.BLACK
      else:
        b.turn = b.WHITE
    # MonteCarlo's Turn
    elif b.turn == AI2.color:
      AI2.Select(b)
      AI2.Expand()
      num = AI2.Choice()
      #print(num)
      sx = b.SearchBoard(b.turn)[num][0]
      sy = b.SearchBoard(b.turn)[num][1]
      #print([sx, sy])
      #print(b.SearchBoard(b.turn))
      b.PutPiece(sx, sy)
      if b.turn == b.WHITE:
        b.turn = b.BLACK
      else:
        b.turn = b.WHITE

    #quit/command
    for event in pg.event.get():
      if event.type == QUIT:
        pg.quit()
        sys.exit()
      if event.type == MOUSEBUTTONDOWN and event.button == 1:
        x, y = event.pos
        sx = (x - 200) // 80
        sy = y // 80
        print("----------")
        print(b.CheckBoard(sx, sy, b.turn))
        print([sx, sy])
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
  main()
