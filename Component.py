from typing import Self

class Node:
    def __init__(self, 
            ares: tuple[int, int], 
            stones: list[tuple[int, int, int]], 
            parent: Self = None, 
            weight: int = 0, 
            dir: str = ""):
        self.ares = ares
        self.stones = stones
        self.parent = parent
        self.weight = weight
        self.dir = dir
    
    def get_state(self) -> tuple[tuple[int, int], tuple[list[tuple[int, int, int]]]]:
        return (self.ares, frozenset(self.stones))
    
    def get_path(self) -> str:
        path = ""
        curr = self

        while (curr.parent):
            path += curr.dir
            curr = curr.parent

        path += curr.dir

        return path[::-1]
    
    def __str__(self) -> str:
        return f"Weight={self.weight} | Ares={self.ares} | Stones={frozenset(self.stones)} | Dir={self.dir}"
    
    def __lt__(self, other: Self) -> bool:
        return self.weight < other.weight

class Grid:
    def __init__(self, walls: list[tuple[int, int]], switches: list[tuple[int, int]]):
        self.walls = walls
        self.switches = switches