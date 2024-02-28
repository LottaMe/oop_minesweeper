from abc import ABC, abstractmethod
class Cell(ABC):
    def __init__(self) -> None:
        self.is_revealed = False

    def reveal(self) -> None:
        self.is_revealed = True

    @abstractmethod
    def show(self) -> None:
        pass
    
class MineCell(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.is_mine = True
    
    def reveal(self) -> None:
        super().reveal()
    
    def show(self) -> str:
        if self.is_revealed:
            return 'm'
        else:
            return '?'

class SafeCell(Cell):
    instances = []
    def __init__(self) -> None:
        super().__init__()
        self.adjacent_mines = 0
        SafeCell.instances.append(self)

    def reveal(self) -> None:
        return super().reveal()
    
    def show(self) -> str:
        if self.is_revealed:
            return str(self.adjacent_mines)
        else:
            return '?'

    def increase_adjacent_mines(self) -> None:
        self.adjacent_mines = self.adjacent_mines + 1
