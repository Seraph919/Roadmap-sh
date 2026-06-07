from random import randrange
import sys

def display_board(board):
    horizontal_border = "+-------+-------+-------+"
    empty_row         = "|       |       |       |"
    
    for i in range(3):
        print(horizontal_border)
        print(empty_row)
        print(f"|   {board[i][0]}   |   {board[i][1]}   |   {board[i][2]}   |")
        print(empty_row)
    print(horizontal_border)




def make_list_of_free_fields(board):
    free = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                free.append((i, j))
    return free


def enter_move(board):
    while True:
        user_input = input("Enter your move (1-9) or EXIT to exit: ").strip().upper()
        
        if user_input == "EXIT":
            print("Thanks for playing!")
            sys.exit()
            
        if not user_input.isdigit() or not ('1' <= user_input <= '9'):
            print("Invalid input. Please enter a single number from 1 to 9.")
            continue
            
        num = int(user_input)
        x = (num - 1) // 3
        y = (num - 1) % 3
        
        if (x, y) in make_list_of_free_fields(board):
            board[x][y] = 'O'
            break
        else:
            print("That square is already filled. Try again.")
            
    display_board(board)



def victory_for(board, sign):
    for row in board:
        if row[0] == row[1] == row[2] == sign:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == sign:
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False



def draw_move(board):

    print("Computer's turn:")
    free = make_list_of_free_fields(board)
    if (len(free) > 0):
        index = randrange(len(free))
        x = free[index][0]
        y = free[index][1]
        board[x][y] = 'X'
    display_board(board)



firstMove = True

board = [['1', '2', '3'],
         ['4', '5', '6'],
         ['7', '8', '9']]

board[1][1] = 'X'

while True:
    enter_move(board)

    if victory_for(board, 'O'):
        print("You won!")
        break
    
    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break

    draw_move(board)
    
    if victory_for(board, 'X'):
        print("Computer won!")
        break

    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break