#!/usr/bin/env python3

from .board import Board
from .protocol import checkCommand
from .printFlush import printFlush

def loop():
    plate = Board(0)
    while 1:
        try:
            command = input()
            checkCommand(command, plate)
        except EOFError:
            break
        except Exception as error:
            if error.__str__() != "":
                printFlush("ERROR " + error.__str__())