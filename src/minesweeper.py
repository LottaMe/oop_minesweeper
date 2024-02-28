from .cells import MineCell, SafeCell
from .input_handler import InputHandler
from .mine_generator import MineGenerator

class Minesweeper:
    def __init__(
            self, 
            rows:int, 
            cols:int, 
            mine_generator:MineGenerator, 
            input_handler: InputHandler
        ) -> None:
        self.rows = rows
        self.cols = cols
        self.mine_generator = mine_generator
        self.input_handler = input_handler
        self.grid = [[SafeCell() for _ in range(self.cols)] for _ in range(self.rows)]

    def __reveal_cell(self, row:int, col:int):
        current_cell:SafeCell or MineCell = self.grid[row][col]
        if current_cell.is_revealed:
            return True
        
        elif isinstance(current_cell, MineCell):
            current_cell.is_revealed = True
            return False
        
        else:
            self.__count_adjacent_mines(row=row, col=col)
            current_cell.is_revealed = True
            return True

    def __count_adjacent_mines(self, row:int, col:int) -> int:
        current_cell:SafeCell = self.grid[row][col]
        surrounding_cells = [
            (row-1, col-1),
            (row-1, col),
            (row-1, col+1),
            (row, col-1),
            (row, col+1),
            (row+1, col-1),
            (row+1, col),
            (row+1, col+1),
        ]
        for cell in surrounding_cells:
            if(cell[0]>=0 and cell[0]<self.rows and cell[1]>= 0 and cell[1] < self.cols):
                if(isinstance(self.grid[cell[0]][cell[1]], MineCell)):
                    current_cell.adjacent_mines += 1
        
    def __reveal_all(self):
        for i, row in enumerate(self.grid):
            for j,_ in enumerate(row):
                self.__reveal_cell(i, j)

    def __display_grid(self) -> None:
        for row in self.grid:
            for cell in row:
                print(cell.show(), end=" ")
            print()
    
    def __check_win(self):
        filtered_instances = []
        for instance in SafeCell.instances:
            if not instance.is_revealed:
                filtered_instances.append(instance)
        return len(filtered_instances) == self.mine_generator.mine_count
    
    def play(self) -> None:
        self.__display_grid()
        self.mine_generator.place_mines(self.grid)

        while True:
            row_index = self.input_handler.get_valid_input(max=self.rows)
            col_index = self.input_handler.get_valid_input(max=self.cols)
            
            if not self.__reveal_cell(row=int(row_index), col=int(col_index)):
                print("you lost")
                self.__reveal_all()
                self.__display_grid()
                break

            if self.__check_win():
                print("You won!")
                self.__reveal_all()
                self.__display_grid()
                break

            self.__display_grid()