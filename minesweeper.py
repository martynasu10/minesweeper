from board import *

class minesweeper:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack()
        
        self.new_board = board(10, 10, 2)
        self.buttons = {}
        self.create_widgets()
        
    def create_widgets(self):
        for x in range(self.new_board.rows):
            for y in range(self.new_board.cols):
                btn = tk.Button(self.frame, width=2, height=1)
                btn.grid(row=x, column=y)
                
                btn.bind('<Button-1>', lambda event, x=x, y=y: self.left_click(x, y))
                btn.bind('<Button-3>', lambda event, x=x, y=y: self.right_click(x, y))
                
                self.buttons[(x,y)] = btn
        
    def left_click(self, x, y):
        non_mine = self.new_board.reveal(x, y)
        if non_mine:
            for a, b in non_mine:
                btn = self.buttons[(a,b)]
                num = self.new_board.grid[0, a, b]
                btn.config(
                text=str(num) if num > 0 else '',
                fg=colors.get(num, 'black') if num > 0 else 'black',
                disabledforeground=colors.get(num, 'black') if num > 0 else 'black',
                bg='lightgrey', 
                state='disabled')
                    
        else:
            self.buttons[(x,y)].config(text='💣', bg='red')
        
    def right_click(self, x, y):
        
        btn = self.buttons[(x,y)]
        curr = btn.cget('text')
        
        if self.new_board.grid[2, x, y] == 0:
            if curr == '':
                btn.config(text='🚩')
            elif curr == '🚩':
                btn.config(text='')
        self.new_board.flag(x, y)

        
    

if __name__ == "__main__":
    
    r = tk.Tk()
    r.title("Minesweeper")
    game = minesweeper(r)
    r.mainloop()