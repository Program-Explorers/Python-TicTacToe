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

#Ask for user_input and validate it
def user_choice_row(char):
    choice_row = 'WRONG'
    
    while choice_row.isdigit() == False:
    
        choice_row = input(f"\nType in the ROW you would like to place your '{char}': ")
        
        if choice_row.isdigit() == False:
            print('Sorry that is not a valid number. Please type a number from 1 and 3')
            
    return int(choice_row)
    

def user_choice_col(char):
    choice_col = 'NOPE'
    
    while choice_col.isdigit() == False:
        
        choice_col = input(f"Type in the COLUMN you would like to place your '{char}': ")
        
        if choice_col.isdigit() == False:
            print('Sorry that is not a valid number. Please type a number from 1 and 3')
            
    return int(choice_col)
    
    

    
    
#checks if the user won by a row

def row_win():
    pass
    
def col_win():
    pass
    
def diag_win():
    pass
    
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
    
        input_row = user_choice_row(character)
        
        input_col = user_choice_col(character)
    
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
