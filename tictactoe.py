#Main Code here

#importing libraries
import numpy as np
import random


#functions

#Creates a board
board = []

for x in range(0, 3):
  board.append(["0"] * 3)

def print_board(board):
  for row in board:
    print(' '.join(row))



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
    print('\n\nWelcome to Tic Tac Toe!\nYou will be playing with a computer!\nFirst to three wins')

    #Randomizes character assignment X or O
    if result == 1:
        print('\nYou are X!\n')
        character = 'X'
        
    elif result == 2:
        print('\nYou are Y!\n')
        character = 'X'
        
    else:
        print('Error in choosing your character XO')
    
    for turn in range(10):
        print_board(board)

        print('\n Turn:', turn+1)

        #Gathers input for row and column
        input_row = int(input(f"\nType in the ROW you would like to place your '{character}': "))
        input_col = int(input(f"Type in the COLUMN you would like to place your '{character}':"))

    
        if user_wins == 3:
            print('You have won! Great Job!')
            break
        elif comp_wins ==3:
            print('The computer has won! Better luck next time.')
            break
        
        else:
            if input_row not in range(1,4) or input_col not in range(1,4):
                print('\n  OOPS, thats not on the board')
            
            elif board[input_row-1]==character or [input_col-1] == character:
                print('\n  You have guessed that already')
                
            else:
                board[input_row-1][input_col-1] = character
                
                        
            
    
        
    
    
        



if __name__ == "__main__":
    main()
