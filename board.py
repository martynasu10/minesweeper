import numpy as np
import random as rand
import tkinter as tk
from definitions import *
from collections import deque


rand.seed(0)
class board:
    def __init__(self, ROWS=10, COLS=10, DIFF=1):
        self.rows = ROWS
        self.cols = COLS
        self.diff = DIFF
        self.flags = 0
        self.mines = int(np.ceil(ROWS * COLS * (DIFF * 0.04 + 0.1)))
        self.grid = np.zeros((3, ROWS, COLS), dtype=int)
        self.buttons = {}
        
            #grid is an array -> 3 layers x rows x cols;
            #layer 0: adj mines
            #layer 1: mines
            #layer 2: reveal/flag grid
        
        self.set_mines()
        self.set_nums()
       
    def set_mines(self):
        m = self.mines
        
        while m > 0:
            x, y = rand.randint(0, self.rows-1), rand.randint(0, self.cols-1)
            
            if self.grid[1, x, y] != 1:
                self.grid[1, x, y] = 1
                m -= 1
                
    def set_nums(self):
        for x in range(self.rows):
            for y in range(self.cols):
                self.grid[0, x, y] = self.count_neighbours(x, y)
                
    def count_neighbours(self, x, y):
        
        count = 0
        for dx, dy in directions:
            if 0 <= x+dx < self.rows and 0 <= y+dy < self.cols:
                if self.grid[1, x+dx, y+dy] == 1:
                    count += 1
        return count
    
    def reveal(self, x, y): #return list (x0y0, x1y1, x2y2)
        queue = deque()
        queue.append((x,y))
        
        out = []
        while queue:
            
            xn, yn = queue.popleft()
            if not (xn, yn) in out:
                out.append((xn, yn))
            
            if self.grid[1, xn, yn] == 1:
                return False
            
            self.grid[2, xn, yn] = 1
            
            if self.grid[0, xn, yn] == 0:
                for xd, yd in directions:
                    if 0 <= xn+xd < self.rows and 0 <= yn+yd < self.cols:
                        if self.grid[2, xn+xd, yn+yd] == 0:
                            queue.append((xn+xd, yn+yd))
        return out
                                
        
        
    def flag(self, x, y):
        
        #layer 2 conditions
        #0 = unrevealed => flag
        #1 = revealed no mine -> do nothing
        #2 = flag -> unflag
        
        if self.grid[2, x, y] == 0:
            self.grid[2, x, y] = 2
            self.flags += 1
            
        elif self.grid[2, x, y] == 1:
            return False
        
        elif self.grid[2, x, y] == 2:
            self.grid[2, x, y] = 0
            self.flags -= 1