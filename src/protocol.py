#!/usr/bin/env python3

from .board import Board, turn
from .printFlush import printFlush
from .ai.basic import print_random
import random

import re

boardCommand = False
begin = False
player = 2

def checkStart(command: str, plate:Board):
    if (command.split()[0] != "START"):
        raise Exception("board mut be initialized with command START")
    if (len(list(command.split(" "))) != 2):
        raise Exception("command START: size must be specified: START size")
    sizeBord = int(list(command.split(" "))[1])
    if (sizeBord < 5 or sizeBord > 20):
        raise Exception(f"command START: size must be between 5 and 20 but received {sizeBord}")
    plate.resize(sizeBord)
    printFlush("OK")

def checkTurn(command: str, plate:Board):
    if (not re.match("^TURN [0-9]+,[0-9]+$", command)):
        raise Exception
    words = re.findall("[\w]+", command)
    words[1] = int(words[1])
    words[2] = int(words[2])
    if player == 1:
        turn(plate, words[1], words[2], 2)
    else:
        turn(plate, words[1], words[2], 1)
    print_random(plate, player)

def checkBoard(command:str, plate:Board):
    global boardCommand
    global player
    player = 1
    if (command.split()[0] == "BOARD" and len(command.split()) != 1):
        raise Exception
    if (command.split()[0] == "DONE" and len(command.split()) != 1):
        raise Exception
    if command == "BOARD":
        boardCommand = True
        return
    if command == "DONE":
        boardCommand = False
        print_random(plate, player)
        return
    if (not re.match("^[0-9]+,[0-9]+,[0-9]+$", command)):
        raise Exception
    words = re.findall("[\w]+", command)
    if (int(words[2]) < 0 or int(words[2]) > 2):
        raise Exception
    turn(plate, int(words[0]), int(words[1]), int(words[2]))

def checkBegin(command: str, plate:Board):
    global begin
    global player
    if (begin):
        raise Exception
    player = 1
    pos = []
    pos = int((plate.size - 1) / 2)
    printFlush(f"{pos},{pos}")
    begin = True
    turn(plate, pos, pos, player)

def checkEnd(command: str, plate:Board):
    exit(0)

def checkDebug(command:str, plate:Board):
    print(plate)

cmd = {"TURN": checkTurn, "BOARD":checkBoard, "END": checkEnd, "START": checkStart, "DEBUG":checkDebug, "BEGIN":checkBegin}

def checkCommand(command:str, plate:Board):
    if boardCommand:
        checkBoard(command, plate)
        return
    if (command.split()[0] not in cmd):
        raise Exception
    cmd[command.split()[0]](command, plate)
