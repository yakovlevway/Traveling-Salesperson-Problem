####################################################
#####################################################Shaxmati
#####################################################
######################################################
from abc import abstractmethod, ABCMeta
import random
THINKING_DEPTH = 5
class Color(object):
    BLACK = 1
    WHITE = 2
    EMPTY = 0
    @classmethod
    def invert(cls, color):
        if color == cls.EMPTY:
            return color
        return cls.BLACK if color == cls.WHITE else cls.WHITE
    
class Doska(object):
    SPACE_COLOR_WHITE = 0
    SPACE_COLOR_BLACK = 45
    board = None
    def fill(self):
        board = self.board = [[PustayaYaheika() for x in range(8)] 
        for y in range(8)] 
        black = Color.BLACK
        white = Color.WHITE
#         a = 0
#         b = 0
#         c = 0
#         while True:
#             a = int(random.randint(0, 7))
#             b = int(random.randint(0, 7))
#             c = int(random.randint(0, 7))
#             if a != b and c != b:
#                 break
#     # simple start position on the board
#         board[int(random.randint(0, 3))][a] = FigureKing(black)
#         board[int(random.randint(4, 7))][c] = FigureKing(white)
#         board[int(random.randint(4, 7))][b] = FigureRook(white)
        board[0][7] = FigureKing(black)
        board[3][7] = FigureKing(white)
        board[1][0] = FigureRook(white)
        
    def clone(self):
        cb = Doska()
        cb.board = [self.board[i][:] for i in range(8)]
        return cb
    
    def get_chessman(self, x, y):
        return self.board[y][x]
    
    def get_color(self, x, y):
        return self.get_chessman(x, y).color
    
    def get_chessman_moves(self, x, y):
        return self.get_chessman(x, y).get_moves(self, x, y)
    
    def move_chessman(self, xy_from, xy_to):
        captured = self.board[xy_to[1]][xy_to[0]]
        self.board[xy_to[1]][xy_to[0]] = self.board[xy_from[1]][xy_from[0]]
        self.board[xy_from[1]][xy_from[0]] = PustayaYaheika()
        return captured
    
    def is_empty(self, x, y):
        return self.get_chessman(y, x).CODE == 'empty'
    
    def rate(self, color): 
        res = 0
        for y in range(8):
            for x in range(8):
                if self.get_color(x, y) != color:
                    continue
                chessman = self.get_chessman(x, y)
                res += chessman.rate(self, x, y)
        return res
    
        
    def __str__(self):
        res = '   a b c d e f g h\n'
        for y in range(8):
            res += "\033[0m" + str(8 - y)
            for x in range(8):
                color = self.SPACE_COLOR_BLACK if (x + y) % 2 else self.SPACE_COLOR_WHITE
                res += ' \033[%sm%s' % (color, self.board[y][x])
            res += " \033[0m " + "\n"
        return res
    
class PustayaYaheika(object):
    CODE = 'empty'
    color = Color.EMPTY
    def get_moves(self, board, x, y):
        raise Exception('Error!')
        
    def rate(self, board, x, y):
        raise Exception('Error!')
        
    def __str__(self):
        return ' '
    
    
class Figure(object):
    __metaclass__ = ABCMeta
    CODE = None
    VALUE = None
    WHITE_IMG = None
    BLACK_IMG = None
    color = None
    def __init__(self, color):
        self.color = color
    @abstractmethod
        
    def get_moves(self, board, x, y):
        return []
    @abstractmethod
        
    def rate(self, board, x, y):
        return 0
    
    def enemy_color(self):
        return Color.invert(self.color)
    
    def __str__(self):
        return self.WHITE_IMG if self.color == Color.WHITE else self.BLACK_IMG
    
class FigureKing(Figure):
    CODE = 'king'
    VALUE = 90
    WHITE_IMG = '♔'
    BLACK_IMG = '♚'
    def get_moves(self, board, x, y):
        moves = []
        for j in (y - 1, y, y + 1):
            for i in (x - 1, x, x + 1):
                if i == x and j == y:
                    continue
                if 0 <= i <= 7 and 0 <= j <= 7 and board.get_color(i, j) != self.color:
                    moves.append([i, j])
        return moves
    
    def rate(self, board, x, y):
        return self.VALUE
    
class FigureRook(Figure):
    CODE = 'rook'
    VALUE = 30
    WHITE_IMG = '♖'
    BLACK_IMG = 'r'
    def get_moves(self, board, x, y):
        moves = []
        for j in (-1, 1):
            i = x + j
            while 0 <= i <= 7:
                color = board.get_color(i, y)
                if color == self.color:
                    break
                moves.append([i, y])
                if color != Color.EMPTY:
                    break
                i += j
        for j in (-1, 1):
            i = y + j
            while 0 <= i <= 7:
                color = board.get_color(x, i)
                if color == self.color:
                    break
                moves.append([x, i])
                if color != Color.EMPTY:
                    break
                i += j
        return moves

    def rate(self, board, x, y):
        return self.VALUE

class AI(object):
    def __init__(self, my_color, depth):
        self.my_color = my_color
        self.enemy_color = Color.invert(my_color)
        self.depth = depth
        
    def do(self, board, depth=0):
        if self.my_color == 1: self.depth = 3
        enemy = bool(depth % 2)
        color = self.enemy_color if enemy else self.my_color
        if depth == self.depth:
            return board.rate(self.my_color) - board.rate(self.enemy_color) * 1.5
        rates = []
        for y in range(8):
            for x in range(8):
                if board.get_color(x, y) != color:
                    continue
                xy_from = [x, y]
                for xy_to in board.get_chessman_moves(x, y):
                    new_board = board.clone()
                    target_cell = new_board.move_chessman(xy_from, xy_to)
                    captured = target_cell.CODE != 'empty'
                    if captured and target_cell.CODE == 'king':
                        rate = -100000 if enemy else 100000
                    else:
                        rate = self.do(new_board, depth + 1)
                        if rate is None:
                            continue
                        if captured and not enemy:
                            rate += self.depth - depth
                    if depth:
                        rates.append(rate)
                    else:
                        rates.append([rate, xy_from, xy_to])
        if not depth:
            return rates
        if not rates:
            return None
        rate = min(rates) if enemy else max(rates)
        return rate



class Game(object):
    @staticmethod
    def clear_screen():
        print("\033[2J\033[1;3H\033[14;0m")
        
    def __init__(self):
        maxrate=[[-999999,0,0]]
        cb = Doska()
        cb.fill()
        self.clear_screen()
        print(cb)
        color = Color.WHITE
        for i in range(50):
            max_rate = -99999
            xy_from = xy_to = None
            rates = AI(color, THINKING_DEPTH).do(board = cb)
            #print(rates)
            for rate in rates:
                if rate[0] < max_rate:
                    continue
                max_rate, xy_from, xy_to = rate
                if max_rate > maxrate[0][0]:
                    maxrate = []
                maxrate.append([max_rate, xy_from, xy_to])
                for i in range (len(maxrate)):
                    if maxrate[i][0] == -99997:
                        maxrate.pop(i)
                leng = len(maxrate)-1
                rnd = random.randint(0, leng)
            maxrate1 = maxrate
            maxrate=[[-999999,0,0]]
            if (maxrate1==[[-999999,0,0]]):
                print('end')
                sys.exit()
            cb.move_chessman(maxrate1[rnd][1], maxrate1[rnd][2])
            color = Color.invert(color)
            self.clear_screen()
            print(cb)
Game()