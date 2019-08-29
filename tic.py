from IPython.display import clear_output
def display_board(board):
    board_blank = [[1,2,3],[4,5,6],[7,8,9]]
    x = 1
    while x <= 9:
        for i in board_blank:
            for j in i:
                i = board[x]
                x = x+ 1
                print(i, end = ' ')
            print()
            

    pass

def player_input():

    player1 = input("Player 1, please pick a marker X or O: ")
    while player1 != 'X' and player1 != 'O':
        player1 = input("Incorrect, please pick a marker X or O: ")
        if player1 == 'X' or player1 == 'O':
            continue
    else:
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
    return player1,player2

def win_check(board, marker):
    
    mark_list = list(marker*3)
    statement = '{} marker won the game! Good for you'. format(marker)
    
    if marker == 'X':
        if mark_list == board[1:4]:
            return statement

        if mark_list == board[4:7]:
            return statement

        if mark_list == board[7:10]:
            return statement

        if mark_list == list([board[1]] + [board[5]] + [board[9]]):
            return statement

        if mark_list == list([board[3]] + [board[5]] + [board[7]]):
            return statement

        if mark_list == list([board[1]] + [board[4]] + [board[7]]):
            return statement

        if mark_list == list([board[2]] + [board[5]] + [board[8]]):
            return statement

        if mark_list == list([board[3]] + [board[6]] + [board[9]]):
            return statement
    
    elif marker == 'O':
        if mark_list == board[1:4]:
            return statement

        if mark_list == board[4:7]:
            return statement

        if mark_list == board[7:10]:
            return statement

        if mark_list == list([board[1]] + [board[5]] + [board[9]]):
            return statement

        if mark_list == list([board[3]] + [board[5]] + [board[7]]):
            return statement

        if mark_list == list([board[1]] + [board[4]] + [board[7]]):
            return statement

        if mark_list == list([board[2]] + [board[5]] + [board[8]]):
            return statement

        if mark_list == list([board[3]] + [board[6]] + [board[9]]):
            return statement
        
    else:
        return False

import random
def choose_first():
    num = random.randint(0,2)
    if num == 1:
        print('Player 1 goes first')
        return 1
    else:
        print('Player 2 goes first')
        return 2

def space_check(board, position):
    return board[position] == 'X' or board[position] == 'O'

def full_board_check(board):
    for pos in board[1:10]:
        if pos == 'X' or pos == 'O':
            pass
        else:
            return False
    return True
    
def player_choice(board):
    position = int(input('Please put in a number from 1-9 to place your marker: '))
    answ = space_check(board,position)
    if answ == False:
        return position
    pass


def replay():
    play = input('Do you want to play again? Y/N')
    if play == 'Y':
        return True
    pass


def TicTacToe():
    print('Welcome to Tic Tac Toe!')
    player1,player2 = player_input()
    print(player1)
    print(player2)
    order = choose_first() 
    board = ['#',1,2,3,4,5,6,7,8,9]
    print(display_board(board))
    space = full_board_check(board)
    
    
    while space == False:
        
        if order == 1:
            position = player_choice(board)
            updated = place_marker(board,player1,position)
            check = win_check(updated,player1)
            print(check)
            print(display_board(updated))
            if check == False:
                break
            else:
                return 'Player 1 won!'
                
            position =  player_choice(board)
            updated = place_marker(updated,player2,position)
            check = win_check(updated,player2)
            print(check)
            print(display_board(updated))
            if check == False:
                break
            else:
                return 'Player 2 won!'
                
        elif order == 2:
            position = player_choice(board)
            updated = place_marker(board,player2,position)
            check = win_check(updated,player2)
            print(check)
            print(display_board(updated))
            if check == False:
                break
            else:
                return 'Player 2 won!'
                
            position =  player_choice(board)
            updated = place_marker(updated,player1,position)
            check = win_check(updated,player1)
            print(check)
            print(display_board(updated))
            if check == False:
                break
            else:
                return 'Player 1 won!'
                
                
        print(display_board(updated))
               
        space = full_board_check(updated)
        print(space)
        