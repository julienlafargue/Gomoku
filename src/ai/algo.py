from ..board import Board
from ..printFlush import printFlush
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

def checkOutOfRangeAlgo(size:int, pos:list) -> bool:
    if pos[0] < 0 or pos[0] >= size or pos[1] < 0 or pos[1] >= size:
        return False
    return True

def random_play_around_pawn(plate:Board, player:int, current):
    error = [-1, -1]
    pos_tab = []
    global dirs

    for i in dirs:
        tmp = [current[0] + i[0], current[1] + i[1]]
        if not checkOutOfRangeAlgo(plate.size, tmp):
            continue
        if plate.board[tmp[1]][tmp[0]] == 0:
            pos_tab.append(tmp)
    if pos_tab == []:
        return error
    tmp = pos_tab[random.randrange(len(pos_tab))]
    return tmp

def verify_possibility(plate:Board, player:int, pos_tab):
    global dirs

    for i in pos_tab:
        tmp = []
        for j in dirs:
            tmp.append(i[0] + j[0])
            tmp.append(i[1] + j[1])
            if checkOutOfRangeAlgo(plate.size, tmp) == False: #verifier les arguments envoyé a la fctn
                continue
            if plate.board[tmp[1]][tmp[0]] == 0:
                return True
    return False

def print_list(list):
    for i in list:
        print(i)

def nearest_move(plate:Board, player:int):
    x:int = 0
    y:int = 0
    tmp = [-1, -1]
    pos_tab = []

    while (y < plate.size):
        while (x < plate.size):
            if (plate.board[y][x] == player):
                pos_tab.append([x, y])
            x += 1
        y += 1
        x = 0
    if verify_possibility(plate, player, pos_tab) == False: #need to be verified
        return [-1, -1]
    if pos_tab != []:
        tmp = random_play_around_pawn(plate, player, pos_tab[random.randint(0, len(pos_tab)-1)])
        while tmp == [-1, -1]:
            tmp = random_play_around_pawn(plate, player, pos_tab[random.randint(0, len(pos_tab)-1)])
    return tmp