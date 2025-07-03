from board import board
import random as rand

directions = [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,0), (-1,-1)]

#initialise boards
rand.seed(0)
t_board = board()


#class 'board' tests
def testBoard():
    
    #initialisation tests
    assert t_board.rows == 10, "Should be 10" 
    assert t_board.cols == 10, "Should be 10"
    assert t_board.diff == 1, "Should be 1"
    assert t_board.mines == 15, "Should be 15"

    #neighbours tests
    count = 0
    for dx, dy in directions:
        if 0 <= 5+dx < 10 and 0 <= 5+dy < 10:
            if t_board.grid[1, 5+dx, 5+dy] == 1:
                count += 1
    assert t_board.count_neighbours(5, 5) == count

    t_board.set_nums()
    assert t_board.grid[0, 1, 4] == 2
    assert t_board.grid[0, 5, 3] == 2        
    assert t_board.grid[0, 5, 5] == 3
    assert t_board.grid[0, 7, 6] == 4

    #reveal tests
    
    assert t_board.grid[1, 6, 5] == 1    #grid: 1=mine 0=empty
    assert t_board.reveal(6, 5) == False #mine returns False
    
    assert t_board.grid[0, 0, 0] == 0
    assert t_board.grid[0, 3, 0] == 1
    assert t_board.grid[0, 3, 6] == 0
    assert t_board.grid[0, 4, 0] == 1
    assert t_board.grid[0, 6, 5] == 3
    assert t_board.grid[0, 9, 5] == 0
    
    #flag tests
    
    assert t_board.grid[2, 0, 0] == 0
    
    assert t_board.flags == 0
    t_board.flag(0, 0)                  #flag unrevealed
    assert t_board.grid[2, 0, 0] == 2
    assert t_board.flags == 1
    
    t_board.flag(0, 0)                  #unflag
    assert t_board.grid[2, 0, 0] == 0
    assert t_board.flags == 0
    
    t_board.reveal(0, 0)                #reveal
    assert t_board.grid[2, 0, 0] == 1
    
    t_board.flag(0, 0)                  #flag reavealed (do nothing)
    assert t_board.grid[2, 0, 0] == 1
    
    
if __name__ == "__main__":
    testBoard()
    print("Everything passed")