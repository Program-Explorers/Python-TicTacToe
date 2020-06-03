#Main Code here

#importing libraries
# import numpy as np
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

#Ask for user_input and validate it
def user_choice_row(char):
    choice_row = 'WRONG'
    
    while choice_row.isdigit() == False:
    
        choice_row = input(f"Type in the ROW you would like to place your '{char}': ")
        
        if choice_row.isdigit() == False:
            print('Sorry that is not a valid number. Please type a number from 1 and 3')
            
    return int(choice_row)
    

def user_choice_col(char):
    choice_col = 'NOPE'
    
    while choice_col.isdigit() == False:
        
        choice_col = input(f"\nType in the COLUMN you would like to place your '{char}': ")
        
        if choice_col.isdigit() == False:
            print('Sorry that is not a valid number. Please type a number from 1 and 3')
            
    return int(choice_col)
    
    

    
<<<<<<< HEAD
=======
    
#checks if the user won by a row

def row_win(board, row, character):

    if row == 1:
        if board[0] == character and board[1] == character and board[2] == character: 
            return True
            
    elif row == 2:
        if board[3] == character and board[4] == character and board[5] == character:
            return True
            
    elif row == 3:
        if board[6] == character and board[7] == character and board[8] == character:
            return True
            
    else:
        return False
        
def col_win(board, col, character):
    
    if col == 1:
        if board[0] == character and board[3] == character and board[6] == character:
            return True
            
    elif col ==2:
        if board[1] == character and board[4] == character and board[7] == character:
            return True
            
    elif col ==3:
        if board[2] == character and board[5] == character and board[8] == character:
            return True
            
    else:
        return False

    
def diag_win(board, diag, character):
    pass
    
>>>>>>> 4cb69338e8091a48bd2ee0591c12ca9612fc50e1
def random_char():
    result = random.randint(1,3)
    
    if result == 1:
        print('\nYou are X!\n')
        character = 'X'
        
    elif result == 2:
        print('\nYou are O!\n')
        character = 'O'
        
    else:
        print('Error in choosing your character XO')
        
    return character
   
#checks if the user won by a row

def row_win(board, row, character):

    if row == 0:
        if board [0] == character and board[1] == character and board[2] == character: 
            return True
            
    elif row == 1:
        if board[3][3] == character and board[4] == character and board[5] == character:
            return True
            
    elif row == 2:
        if board[6][6] == character and board[7] == character and board[8] == character:
            return True
            
    else:
        return False
        
def col_win(board, col, character):
    
    if col == 1:
        if board[0] == character and board[3] == character and board[6] == character:
            return True
            
    elif col ==2:
        if board[1] == character and board[4] == character and board[7] == character:
            return True
            
    elif col ==3:
        if board[2] == character and board[5] == character and board[8] == character:
            return True
            
    else:
        return False

    
def diag_win(board, diag, character):
    pass
    

def main():

    #First to three wins
    user_wins = 0
    comp_wins = 0
    
    #Greeting
    print('\n\nWelcome to Tic Tac Toe!\nYou will be playing with a computer!\nFirst to three wins')

    #Calls function and gets the random character X or O, and assigns it to the variable
    character = random_char()
    
    for turn in range(10):
        print_board(board)

        print('\n Turn:', turn+1)

        #Gathers input for row and column
    
        input_col = user_choice_col(character)
    
        input_row = user_choice_row(character)
        
    
       ## if user_wins == 3:
        ##    print('You have won! Great Job!')
        ##    break
        ##elif comp_wins ==3:
        ##    print('The computer has won! Better luck next time.')
        ##    break
        
       
        if input_row not in range(1,4) or input_col not in range(1,4):
            print('\n  OOPS, thats not on the board')
            
        elif board[input_row-1]==character or [input_col-1] == character:
            print('\n  You have guessed that already')
                
        else:
            board[input_row-1][input_col-1] = character
            
            won_row = row_win(board, input_row, character)
            won_col = col_win(board, input_col, character)
            
            if won_row==True or won_col == True:
                print('You won! Great Job')
                break
            
                
                        
            
    
        
    
    
        



if __name__ == "__main__":
    main()