#Main Code here
# new branch test!
#importing libraries
# import numpy as np
#TEST
import random


#functions

#Creates a board

def make_board(bard):
    for x in range(0, 3):
        bard.append(["_"] * 3)
    bard[2][0]=bard[2][1]=bard[2][2] = " "

def print_board(board):
  for row in board:
    print('|'.join(row))

def computer_char(character):
    if character =='X':
          return 'O'
    elif character == 'O':
          return 'X'


#We can use this function for the computer to win or to block the opponent
def computer_move_row(row1, row2, row3, board, character, look_char):
    row_list = [row1, row2, row3]
    
    for row_num, row in enumerate(row_list):

        check_values = 0
        
        for i in range(0, 3):
  
            if row[i] == character:
                check_values += 1

                
            if check_values == 2:

                #it will then put its character here in place of the dash or space
            
                for j in range(0,3):
  
                    if board[row_num][j] == ' ' or board[row_num][j] == '_':
          
                        board[row_num][j] = look_char
                        return True
    
    return False
                        
            
def computer_move_col(col1, col2, col3, board, character, look_char):
    col_list = [col1, col2, col3]

    for col_num, col in enumerate(col_list): # go through colums (verticle)
        check_values = 0

        for i in range(0, 3):
            if col[i] == character: # see two in a row

                check_values += 1
                
            if check_values == 2:

                for row in range(0, 3): # find empty row (go throw rows again)
                    if board[row][col_num] == ' ' or board[row][col_num] == '_':
                        board[row][col_num] = look_char
                        print(row, col_num)
                        return True
                        
    return False
                        
def computer_move_dia(dia1, dia2, board, character, look_char):
    dia_list = [dia1, dia2]
    print('dia list:',dia_list)
    
    for dia_num, dia in enumerate(dia_list):
        check_values = 0
        print(f'dia num: {dia_num}')
        
        for i in range(0, 3):
            if dia[i] == character:
                check_values += 1
                print('character')
                
        if check_values == 2:
            print('should win or block')
            
            for row in range(0, 3):
            
                if board[row][2-row] == ' ' or board[row][2-row] == '_':
                    print('going to win or block now')
                    print(row,2-row)
                    board[row][2-row] = look_char
                    return True
                    
                elif board[row][row] == ' ' or board[row][row] == '_':
                    print('going to win or block now')
                    print(row,row)
                    board[row][row] = look_char
                    return True
    return False


def comp_move_random(board, character, look_char):
    x = 0
    y = 0
    
    while board[x][y] == character or board[x][y] == look_char:
        x = random.randint(0,2)
        y = random.randint(0,2)

    board[x][y] = character
    

#Ask for user_input and validate it
def user_choice_row(char):
    choice_row = 10
    
    while choice_row not in range(1,3):
        
        choice_row = int(input(f"Type in the ROW you would like to place your '{char}': "))
        
        if choice_row not in range(1,3):
            print('Sorry that is not a valid number. Please type a number from 1 and 3')
            
    return choice_row
    

def user_choice_col(char):
    choice_col = 11
    
    while choice_col not in range(1, 4):
        
        choice_col = int(input(f"\nType in the COLUMN you would like to place your '{char}': "))
        
        if choice_col not in range(1, 4):
            print('Sorry that is not a valid number. Please type a number from 1 and 3')
            
    return choice_col
    
    

    
#checks if the user won by a row

def row_win(board, row, character):

    if row == 1:
        if board[0][0] == character and board[0][1] == character and board[0][2] == character:
            return True
            
    elif row == 2:
        if board[1][0] == character and board[1][1] == character and board[1][2] == character:
            return True
            
    elif row == 3:
        if board[2][0] == character and board[2][1] == character and board[2][2] == character:
            return True
            
    else:
        return False
        
def col_win(board, col, character):
    
    if col == 1:
        if board[0][0] == character and board[1][0] == character and board[2][0] == character:
            return True
            
    elif col ==2:
        if board[0][1] == character and board[1][1] == character and board[2][1] == character:
            return True
            
    elif col ==3:
        if board[0][2] == character and board[1][2] == character and board[2][2] == character:
            return True
            
    else:
        return False

    
def diag_win(board, row, col ,character):
    if (row ==1 and col ==1)  or   (row ==2 and col ==2)  or  (row==3 and col==3):
        if board[0][0] == character and board[1][1]== character and board[2][2] == character:
            return True
            
    elif (row==3 and col==1)  or  (row==2 and col==2)  or  (row==1 and col==3):
        if board[2][0] == character and board[1][1] ==character and board[0][2]:
            return True
            
    else:
        return False
    

def random_char():
    result = random.randint(1,2)
    character = 'default'
    if result == 1:
        print('\nYou are X!\n')
        character = 'X'
        
    elif result == 2:
        print('\nYou are O!\n')
        character = 'O'
        
    else:
        print('Error in choosing your character XO')
    return character
   
# Checks if user wants to play again
def gameon():
    again = 'wrong'
    chosen = False
    acceptable_values = ['Y', 'y', 'yes','Yes']
    un_acceptable_values = ['n', 'N', 'No', 'no']
    
    while again not in acceptable_values or again not in un_acceptable_values:
        again = input('Would you like to play again? (Y/N) ')
        
        if again not in acceptable_values or again not in un_acceptable_values:
            print('Please type Y or N')

        if again in acceptable_values:
            chosen = True
            return chosen

        elif again in un_acceptable_values:
            chosen = False
            return chosen
     
   
def character_swap(player1):
    if player1:
        return True
    
    return False
    

def win_func(comp, board):
    print('win func')
    print('\n'*100)
    print('*---------------------------------Tic-Tac-Toe----------------------------------*\n')

    if comp:
        print_board(board)
        print('\nThe computer won! Better luck next time.')
        
    else:
        print_board(board)
        print('\nYou won! Great Job')
    


def main():
    board = []
    make_board(board)
    game_on = True
    character ='X'
    
    
    player1 = True
    is_user = True
    possibles_choice = ['Y','y', 'Yes', 'yes']
    
    #While the user want to play
    while game_on == True:
        
        
        print('\n'*100)
        print('*---------------------------------Tic-Tac-Toe----------------------------------*\n\n')

        print('\n\nWelcome to Tic Tac Toe!\nYou will be playing with a computer or with friend!\n')

        choice = input('Do you want to play with the computer? (Y/N): ')

        if choice in possibles_choice:
            computer_yes = True

        elif choice not in possibles_choice:
            computer_yes = False

        else:
            print('Please write Y or N')



        while computer_yes:
            
            print('\n'*100)
            print('*---------------------------------Tic-Tac-Toe----------------------------------*\n')
            print_board(board)
        
        
            #user
            if is_user == True:
                if character == 'X':
                    opp_char = 'O'
                else:
                    opp_char == 'X'
                print("\nYour turn now")
                is_user = False
                
                #Gathers input for row and column
                input_col = user_choice_col(character)
                input_row = user_choice_row(character)
                           
                          
                if input_row not in range(1,4) or input_col not in range(1,4):
                    print('\n  OOPS, thats not on the board')
                               
                elif board[input_row-1][input_col-1]==character:
                    print('\n  You have guessed that already')
                                   
                else:
                    while board[input_col-1][input_row-1] == opp_char or board[input_col-1][input_row-1] == character:
                        print('\nSorry that spot is already TAKEN')
                        input_col = user_choice_col(character)
                        input_row = user_choice_row(character)
                
                    print('place:', board[input_row-1][input_col-1])
                    board[input_row-1][input_col-1] = character
                               
                    won_row = row_win(board, input_row, character)
                    won_col = col_win(board, input_col, character)
                    won_diag = diag_win(board, input_row, input_col, character)
                               
                if won_row==True or won_col == True or won_diag ==True:
                    print('\n'*100)
                    print('*---------------------------------Tic-Tac-Toe----------------------------------*\n')
                    print_board(board)
                    print('\nYou Won! Great Job\n')
                    break
                                           
                
                
                
              #computer
            if is_user == False:
                is_user = True
                row1 = board[0]
                row2 = board[1]
                row3 = board[2]
               
                col1 = [board[0][0], board[1][0], board[2][0]]
                col2 = [board[0][1], board[1][1], board[2][1]]
                col3 = [board[0][2], board[1][2], board[2][2]]
               
                dia1 = [board[0][0], board[1][1], board[2][2]]
                dia2 = [board[0][2], board[1][1], board[2][0]]
                
                if character == 'X':
                    look_char = 'O'
                else:
                    look_char == 'X'
                    
                print("It's the computer's turn")
                comp_row1 = computer_move_row(row1, row2, row3, board, look_char, look_char)
                if comp_row1:
                    win_func(True, board)
                    break
                    
                comp_col1 = computer_move_col(col1,col2, col3, board, look_char, look_char)
                if comp_col1:
                    win_func(True, board)
                    break
                    
                comp_dia1 = computer_move_dia(dia1, dia2, board, look_char, look_char)
                if comp_dia1:
                    win_func(True, board)
                    break
    
            
                comp_row2 = computer_move_row(row1, row2, row3, board, character, look_char)
                if comp_row2:
                    continue
                    
                comp_col2 = computer_move_col(col1,col2, col3, board, character, look_char)
                if comp_col2:
                    continue
                    
                comp_dia2 = computer_move_dia(dia1, dia2, board, character, look_char)
                if comp_dia2:
                    continue
                    

                comp_move_random(board, look_char, character)
                
                
                
            
      
                
        while computer_yes == False:
        
            print('\n'*100)

            print('*---------------------------------Tic-Tac-Toe----------------------------------*\n')

            
            row1 = board[0]
            row2 = board[1]
            row3 = board[2]
            
            col1 = [board[0][0], board[1][0], board[2][0]]
            col2 = [board[0][1], board[1][1], board[2][1]]
            col3 = [board[0][2], board[1][2], board[2][2]]
            
            dia1 = [board[0][0], board[1][1], board[2][2]]
            dia2 = [board[0][2], board[1][1], board[2][0]]
            
            print_board(board)
            
            if character_swap(player1):
                character = 'X'
                
            elif character_swap(player1)==False:
                character = 'O'
                
            if player1:
                print("\nPlayer 1's turn")
                player1 = False
                #Gathers input for row and column
                input_col = user_choice_col(character)
        
                input_row = user_choice_row(character)
            
           
                if input_row not in range(1,4) or input_col not in range(1,4):
                    print('\n  OOPS, thats not on the board')
                
                elif board[input_row-1][input_col-1]==character:
                    print('\n  You have guessed that already')
                    
                else:
                    board[input_row-1][input_col-1] = character
                
                    won_row = row_win(board, input_row, character)
                    won_col = col_win(board, input_col, character)
                    won_diag = diag_win(board, input_row, input_col, character)
                
                    if won_row==True or won_col == True or won_diag ==True:
                        print('\n'*100)
                        print('*---------------------------------Tic-Tac-Toe----------------------------------*\n')
                        print_board(board)
                        print('\nPlayer 1 won! Great Job\n')
                        break
                            
        
            elif player1 == False:
                print("\nPlayer 2's turn")
                player1 = True
                #Gathers input for row and column
                input_col = user_choice_col(character)
                
                input_row = user_choice_row(character)
                    
                   
                if input_row not in range(1,4) or input_col not in range(1,4):
                    print('\n  OOPS, thats not on the board')
                        
                elif board[input_row-1][input_col-1]==character:
                    print('\n  You have guessed that already')
                            
                else:
                    board[input_row-1][input_col-1] = character
                    
                    won_row = row_win(board, input_row, character)
                    won_col = col_win(board, input_col, character)
                    won_diag = diag_win(board, input_row, input_col, character)
                        
                    if won_row==True or won_col == True or won_diag ==True:
                        print('\n'*100)
                        print('*---------------------------------Tic-Tac-Toe----------------------------------*\n')
                        print_board(board)
                        print('\nPlayer 2 won! Great Job\n')
                        break
             
             
             
        game_on = gameon()
                
                
        if game_on == True:
            print('Alright lets do it again\n')
            board = []
            make_board(board)
                        
        elif game_on == False:
            print('Thanks for playing!\n')
            break
            
                
            
        
    
    
        



if __name__ == "__main__":
    main()
