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

#Make function here: Chooses a random place for the computer

#checks if the user won by a row

def row_win():
    pass
    
def col_win():
    pass
    
def diag_win():
    pass
    
def random_char():
    return random.randint(1,2)
   
def main():
    #First to three wins
    user_wins = 0
    comp_wins = 0
    
    #assigns randome number 1 or 2 to result
    result = random_char()
    #Greeting
    print('\n\nWelcome to Tic Tac Toe!\nYou will be playing with a computer!\n First to three wins')
    
    #Randomizes character assignment X or O
    if result == 1:
        print('You are X!\n')
        character = 'X'
    elif result == 2:
        print('You are Y!\n')
        character = 'X'
    else:
        print('Error in choosing your charcter XO')
    
    #Gathers input for row and column
    input_row = int(input(f"Type in the ROW you would like to place your '{character}': "))
    input_col = int(input(f"Type in the COLUMN you would like to place your '{character}':"))
    
    
        

if __name__ == "__main__":
    main()
