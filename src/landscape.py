from noise import pnoise2
from random import randrange

class Map:
    def __init__(self, size: list | tuple = [0, 0]) -> None:
        self.size: list | tuple = size
        self.map: list = []
        self.generate_map()
    
    def generate_map(self) -> None:
        self.map =  [[0 for i in range(self.size[0])] for i in range(self.size[1])]

    def generate_wm(self, fqc: float = 0.5) -> None:
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                choice: int = randrange(0, 10)
                self.map[y][x] = 0 if choice / 10  <= fqc else 1    
    
    def generate_pm(self) -> None:
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                self.map[y][x] = abs(pnoise2(x / 10, y / 10, octaves=12))
        print(self.map)
