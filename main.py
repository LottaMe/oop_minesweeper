from src.minesweeper import MineGenerator, Minesweeper, InputHandler

if __name__ == "__main__":
    ROWS = 4
    COLS = 4
    MINECOUNT = 4

    mine_generator = MineGenerator(rows=ROWS, cols=COLS, mine_count=MINECOUNT)
    input_handler = InputHandler()
    minesweeper = Minesweeper(
        rows=ROWS, 
        cols=COLS, 
        mine_generator=mine_generator, 
        input_handler=input_handler
    )
    
    minesweeper.play()
