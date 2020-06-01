#Main Code here

#importing libraries
import numpy as np
import random


#functions

#Creates a board
def create_board():
    return(np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))

# Check for empty places on board
#Copied this from interent... you can change if you want
def possibilities(board):
    l = []
      
    for i in range(len(board)):
        for j in range(len(board)):
              
            if board[i][j] == 0:
                l.append((i, j))
    return(l)
