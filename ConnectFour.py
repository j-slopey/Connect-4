# Author: James Slopey

from tkinter import *
import random
import time

class ConnectFour():
    
    def __init__(self):
        # Set up the root window, frame, and canvas
        self.tk = Tk()
        self.tk.title("Connect Four")
        self.tk.resizable(0, 0)
        # Create the frame and initialize the grid layout manager
        frame = Frame(self.tk)
        frame.grid()
        # Create a canvas to indicate which player
        self.canvasPlayer = Canvas(frame, width=675, height=50)
        self.canvasPlayer.grid(row = 1, column = 1)
        # Create a canvas for the connect four grid board
        self.canvas = Canvas(frame, width=675, height=580)
        self.canvas.grid(row=2, column=1)
        
# ->    # Draw the grid on the canvas
        #ROWS
        self.canvas.create_rectangle(10,10,640,100, outline = 'blue')
        self.canvas.create_rectangle(10,100,640,190, outline = 'blue')
        self.canvas.create_rectangle(10,190,640,280, outline = 'blue')
        self.canvas.create_rectangle(10,280,640,370, outline = 'blue')
        self.canvas.create_rectangle(10,370,640,460, outline = 'blue')
        self.canvas.create_rectangle(10,460,640,550, outline = 'blue')

        #COLUMNS
        self.canvas.create_rectangle(10,10,100,550, outline = 'blue')
        self.canvas.create_rectangle(100,10,190,550, outline = 'blue')
        self.canvas.create_rectangle(190,10,280,550, outline = 'blue')
        self.canvas.create_rectangle(280,10,370,550, outline = 'blue')
        self.canvas.create_rectangle(370,10,460,550, outline = 'blue')
        self.canvas.create_rectangle(460,10,550,550, outline = 'blue')
        self.canvas.create_rectangle(550,10,640,550, outline = 'blue')

        
        
        #   (the supplied discs are 90 pixels in diameter)        
        # Bind the mouse button to play
        self.canvas.bind_all("<Button-1>", self.choose)
        # Create the images of the playing pieces
        self.redimage = PhotoImage(file="red.gif")
        self.greenimage = PhotoImage(file="green.gif")
        # Set up the stop button
        self.stopb = Button(frame, text="Close", command=self.endProgram)
        self.stopb.grid(row=3, column=1)
        self.stop = False
        # Initialize class variables
        self.play = [[0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0]]
        self.player = 1
        self.gameOver = False
        self.turn = ["It's Player 1's Turn", "It's Player 2's Turn"]
        self.pturn = self.canvasPlayer.create_text(338, 25, text=self.turn[0], font=("Arial", "20"))
        self.winner = 0

    
    def endProgram(self):
        # Method called with stop buttion pressed
        self.stop = True

    def choose(self, evt):
        column = 0
        row = 0

# ->    # Check that the game is not over
        if self.gameOver:
            return
        
        # Check that the mouse was clicked on the game board
        
        # Determine which column was clicked on by the player
        if evt.x > 10 and evt.x < 640 and evt.y < 640:
            if evt.x < 100:
                column = 0
            if evt.x > 100:
                column = 1
                if evt.x >190:
                    column = 2
                    if evt.x > 280:
                        column = 3
                        if evt.x > 370:
                            column = 4
                            if evt.x > 460:
                                column = 5
                                if evt.x > 550:
                                    column = 6
        
        

        # Place the player appropriate disc in the lowest empty slot
        self.findEmptySlot(column,self.player)
        # Update the play board matrix with the current player
        # Determine if the player won and take appropriate action
        # Switch players
        # Change the message to indicate the current player
        


        

    def placeDisc(self, row, column, player):
        # This is a helper method called from self.choose
# ->    # Determine the correct x and y values for placing the images based on
        x = 0
        y = 0
        
        if column == 0:
            x = 55
        elif column == 1:
            x = 145
        elif column == 2:
            x = 235
        elif column == 3:
            x = 325
        elif column == 4:
            x = 415
        elif column == 5:
            x = 505
        elif column == 6:
            x = 595
            

        
        if row == 0:
            y = 55
        elif row == 1:
            y = 145
        elif row == 2:
            y = 235
        elif row == 3:
            y = 325
        elif row == 4:
            y = 415
        elif row == 5:
            y = 505
        if x == 0 or y == 0:
            pass
            
        
        
        if self.player == 1:
            self.canvas.create_image(x,y,image = self.redimage)
            self.play[row][column] = 1
            self.player = 2
            self.canvasPlayer.itemconfig(self.pturn,text=self.turn[1])
                                   
        elif self.player == 2:
            self.canvas.create_image(x,y,image = self.greenimage)
            self.play[row][column] = 2
            self.player = 1
            self.canvasPlayer.itemconfig(self.pturn,text=self.turn[0])
                    
        self.isWinner()
        
        #    row and column and put them on the canvas
        
            

    def findEmptySlot(self,column,player):
        for x in range(5,-1,-1):
            if self.play[x][column] == 0:
                row = x
                self.placeDisc(row,column,player)
                break
               
        
        # This is a helper method called from self.choose
# ->    # Find the lowest empty slot in the column

        

    def isWinner(self):
        # This is a helper method called from self.choose
        if self.winHorizontal() > 0:
            self.win()
        if self.winVertical() > 0:
            self.win()
        if self.winDiagonal() > 0:
            self.win()
        

    def winHorizontal(self):
        for y in self.play:
            for x in range(4):
                if y[x] == y[x+1] and y[x] == y[x+2] and y[x] == y[x+3] and y[x] == 2:
                    self.winner = 2
                if y[x] == y[x+1] and y[x] == y[x+2] and y[x] == y[x+3] and y[x] == 1:
                    self.winner = 1
        w = self.winner
        return w
        # This is a helper method called from self.isWinner
# ->    # Determine if the player wins with four in a row horizontally



        
    def winVertical(self):
        for x in range(7):
            for y in range(3):
                if self.play[y][x] == 2 and self.play[y+1][x] == 2 and self.play[y+2][x] == 2 and self.play[y+3][x]:
                    self.winner = 2
                if self.play[y][x] == 1 and self.play[y+1][x] == 1 and self.play[y+2][x] == 1 and self.play[y+3][x]:
                    self.winner = 1
        return self.winner
        # This is a helper method called from self.isWinner
# ->    # Determine if the player wins with four in a row vertically



        
    def winDiagonal(self):
        for r in range(3):
            for c in range(4):
                if self.play[r][c] == 2 and self.play[r+1][c+1] == 2 and self.play[r+2][c+2] == 2 and self.play[r+3][c+3] == 2:
                    self.winner = 2
                if self.play[r][c] == 1 and self.play[r+1][c+1] == 1 and self.play[r+2][c+2] == 1 and self.play[r+3][c+3] == 1:
                    self.winner = 1
        for r in range(5,2,-1):
            for c in range(4):
                if self.play[r][c] == 2 and self.play[r-1][c+1] == 2 and self.play[r-2][c+2] == 2 and self.play[r-3][c+3] == 2:
                    self.winner = 2
                if self.play[r][c] == 1 and self.play[r-1][c+1] == 1 and self.play[r-2][c+2] == 1 and self.play[r-3][c+3] == 1:
                    self.winner = 1
        
                    
        return self.winner
        # This is a helper method called from self.isWinner
# ->    # Determine if the player wins with four in a row diagonally

    def win(self):
        self.gameOver = True
        if self.winner == 1:
            self.canvas.create_text(338, 290, text="Player 1 Wins!", font=("Arial", "60"))
            self.canvasPlayer.itemconfig(self.pturn,text="Game Over")

        if self.winner == 2:
            self.canvas.create_text(338, 290, text="Player 2 Wins!", font=("Arial", "60"))
            self.canvasPlayer.itemconfig(self.pturn,text="Game Over")


    def main(self):
        # Main loop that runs the game
        while True:
            time.sleep(.1)
            self.tk.update()
            self.tk.update_idletasks()
            if self.stop == True:
                self.tk.destroy()
                break

# Instantiate the class and run the main method
c4 = ConnectFour()
c4.main()
