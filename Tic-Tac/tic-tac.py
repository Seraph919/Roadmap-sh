from random import randrange


def display_board(board):
    horizontal_border = "+-------+-------+-------+"
    empty_row         = "|       |       |       |"
    
    for i in range(3):
        print(horizontal_border)
        print(empty_row)
        print(f"|   {board[i][0]}   |   {board[i][1]}   |   {board[i][2]}   |")
        print(empty_row)
    print(horizontal_border)


def checkBox(board, num): 
    x = int((num - 1)/ 3)
    y = int((num- 1) % 3)
    if board[x][y] == 'X' or board[x][y] == 'O':
        return False, x, y
    condition = int(board[x][y]) == int(num)
    return  condition, x, y


def make_list_of_free_fields(board):
    free = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                free.append((i, j))
    return free


def enter_move(board):
    while True:
            try:
                Input = input("Enter your move (1-9): ")
                
                if len(Input) != 1 or Input < '1' or Input > '9':
                    print("The number must be greater than 0 and less than 10.")
                    continue
                
                index = ord(Input) - 48
                
                condition, x, y = checkBox(board, index)
                
                if condition == True:
                    board[x][y] = 'O'
                    break
                else:
                    print("Already filled. Try again.")

            except TypeError:
                print("The input must be a Number from 1 to 9.")
            except:
                print("Please enter a Valid input.")



def victory_for(board, sign):
    display_board(board)
    if len(make_list_of_free_fields(board)) == 0:
        print("It's a tie!")
        exit()
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
    global firstMove
    if firstMove == True:
        board[1][1] = 'X'
        firstMove = False
    else:
        free = make_list_of_free_fields(board)
        if (len(free) > 0):
            index = randrange(len(free))
            x = free[index][0]
            y = free[index][1]
            board[x][y] = 'X'



firstMove = True

board = [['1', '2', '3'],['4', '5', '6'],['7', '8', '9']]

while True:
    draw_move(board)

    if victory_for(board, 'X'):
        print("Computer won!")
        break

    enter_move(board)

    if victory_for(board, 'O'):
        print("You won!")
        break