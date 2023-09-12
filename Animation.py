import tkinter as tk

global WIDTH
WIDTH = int(input("Please specify desired animation windows size in pixels: \n"))
root=tk.Tk()
window=tk.Canvas(root, width = WIDTH, height = WIDTH)
window.pack()

class Animation():
    def __init__(self, x1, y1, x2, y2, move1, move2, culoare):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.move1 = move1
        self.move2 = move2
        self.culoare = culoare
        self.patrat = window.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline = "white", fill = f"{self.culoare}") 
    
    def redraw(self):
        window.after(10, self.redraw)
        current_coordinates = window.coords(self.patrat)
        if current_coordinates[0] >= WIDTH or current_coordinates[0] <= -60:
            window.move(self.patrat, -self.move1*WIDTH/2, -self.move2*WIDTH/2)
        else:
            window.move(self.patrat, self.move1, self.move2)
   
blue_suare = Animation(WIDTH/2-20, WIDTH/2-20, WIDTH/2-80, WIDTH/2-80, -1, -1, "blue")
red_square = Animation(WIDTH/2+20, WIDTH/2-20, WIDTH/2+80, WIDTH/2-80, 1,-1, "red")
yellow_square = Animation(WIDTH/2-80,WIDTH/2+80,WIDTH/2-20,WIDTH/2+20, -1,1, "yellow")
green_square = Animation(WIDTH/2 +20,WIDTH/2+20, WIDTH/2+80,WIDTH/2+80, 1,1, "green")
blue_suare.redraw()
red_square.redraw()
yellow_square.redraw()
green_square.redraw()
root.mainloop()
