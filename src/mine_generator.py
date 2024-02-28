import random
from .cells import MineCell

class MineGenerator:
    def __init__(self, rows, cols, mine_count) -> None:
        self.rows = rows
        self.cols = cols
        self.mine_count = mine_count
        self.mine_locations = self.__generate_random_mines()
        
    def __generate_random_mines(self) -> list[int]:
        return random.sample(range(0, self.rows*self.cols), self.mine_count)
    
    def place_mines(self, grid: list[list]) -> list[list]:
        grid_copy = grid.copy()
        for loc in self.mine_locations:
            row = loc//self.rows
            col = loc%self.cols

            grid_copy[row][col] = MineCell()