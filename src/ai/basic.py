from ..board import Board
from ..printFlush import printFlush
from .algo import nearest_move
import random

dirs = [
    [0, -1],
    [1, -1],
    [1, 0],
    [1, 1],
    [0, 1],
    [-1, 1],
    [-1, 0],
    [-1, -1]
]

class Pos:
    x:int
    y:int
    stone:bool
    row:bool

    def __init__(self, x = -1, y = -1) -> None:
        self.x = x
        self.y = y
        self.stone = None
        self.row = False
    def __str__(self) -> str:

        res = f"x:{self.x}, y:{self.y}, play:{self.stone}, row:{self.row}"
        return (res)

def checkOutOfRange(size:int, pos:list) -> bool:
    if pos[0] < 0 or pos[0] >= size or pos[1] < 0 or pos[1] >= size:
        return False
    return True

def checkPlay(plate:Board, stone:int, x:int, y:int, dirx:int, diry:int) -> Pos:
    res = Pos()
    if plate.board[y][x] != stone:
        res.stone = False
    else:
        res.stone = True
    for i in range(1, 5):
        if not checkOutOfRange(plate.size, [x + dirx * i, y + diry * i]):
            break
        if plate.board[y + diry * i][x + dirx * i] == 0:
            res.x = x + dirx * i
            res.y = y + diry * i
            return res
    return res

def checkline(plate:Board, stone:int, x:int, y:int, dirx:int, diry:int) -> Pos:
    res = Pos()
    count = 1
    for i in range(1, 5):
        if (not checkOutOfRange(plate.size, [x + dirx * i, y + diry * i])
            or (plate.board[y + diry * i][x + dirx * i] != 0 and plate.board[y + diry * i][x + dirx * i] != plate.board[y][x])):
            return res
        elif plate.board[y + diry * i][x + dirx * i] == plate.board[y][x]:
            count += 1
    if count > 2:
        res = checkPlay(plate, stone, x, y, dirx, diry)
        if count == 3:
            res.row = True
    return res

def checkDirection(plate:Board, stone:int, turns:list[Pos], x:int, y:int) -> bool:
    global dirs
    for dir in dirs:
        res = Pos()
        if checkOutOfRange(plate.size, [x + dir[0], y + dir[1]]):
            res = checkline(plate, stone, x, y, dir[0], dir[1])
        if res.x != -1 and res.y != -1:
            turns.append(res)
            if res.stone == True and res.row == False:
                return True
    return False

def basic(plate:Board, stone:int) -> list:
    turns:list[Pos] = []
    play:Pos
    for y in range(plate.size):
        for x in range(plate.size):
            play = Pos()
            if plate.board[y][x] != 0:
                if checkDirection(plate, stone, turns, x, y):
                    return [turns[-1].x, turns[-1].y]

    if (len(turns) > 0):
        turns.sort(key=lambda x: x.row)
        turns.sort(key=lambda x: x.stone)
        return [turns[0].x, turns[0].y]
    return []
            

def print_random(plate:Board, player:int):
    pos = basic(plate, player)

    if pos == [] or pos == [-1, -1]:
        pos = nearest_move(plate, player)
    if pos == [] or pos == [-1, -1]:
        while 1:
            pos = [random.randint(0, plate.size - 1), random.randint(0, plate.size - 1)]
            if plate.board[pos[1]][pos[0]] == 0:
                break
    plate.board[pos[1]][pos[0]] = player
    printFlush(f"{pos[0]},{pos[1]}")
