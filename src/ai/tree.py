from src.board import Board
from ..board import Board

class Node:
    name:str
    after:list[str]
    previous:list[str]

    play:list[int]
    value:int

    plate:Board

    def __init__(self, plate:Board, name:str) -> None:
        self.value = 0
        self.plate = plate.copy()
        self.name = name
        self.after = []

class Tree:
    nodes:dict[str,Node]
    actual:str

    def __init__(self, plate:Board) -> None:
        self.actual = "0"
        self.nodes = {self.actual:Node(plate, self.actual)}
