#!/usr/bin/env python3

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Board:
    board: list[list[int]]
    size: int

    def __init__(self, size: int) -> None:
        self.size = size
        self.board = []
        for i in range(size):
            line = []
            for j in range(size):
                line.append(0)
            self.board.append(line)

    def __str__(self) -> str:
        res = "   "
        j = False
        for count in range(self.size):
            res += f" {count}{('', ' ')[count < 10]}"

        count = 0
        for line in self.board:
            res += f"\n{count}{('', ' ')[count < 10]} "
            for pos in line:
                if pos == 1:
                    res += f"{bcolors.RED}[{pos}]{bcolors.END}"
                elif pos == 2:
                    res += f"{bcolors.BLUE}[{pos}]{bcolors.END}"
                else:
                    res += f"[{pos}]"
            count += 1
        return res
    
    def resize(self, size:int):
        self.__init__(size)
    
def turn(board:Board, x:int, y:int, stone:int):
    if (x < 0 or x >= board.size or y < 0 or y >= board.size):
        raise Exception("coordinates out of range")
    board.board[y][x] = stone
