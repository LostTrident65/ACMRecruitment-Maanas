import random

board = [' '] * 10
computer = 'X'
human = 'O'


def disp_board(board):
    print(f'{board[1]} | {board[2]} |{board[3]}')
    print(f'{board[4]} | {board[5]} |{board[6]}')
    print(f'{board[7]} | {board[8]} |{board[9]}')
    print('-' * 10)


def check():
    if board[1] == board[2] == board[3] and board[1] != ' ':
        return True
    elif board[4] == board[5] == board[6] and board[4] != ' ':
        return True
    elif board[7] == board[8] == board[9] and board[7] != ' ':
        return True
    elif board[1] == board[4] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] == board[9] and board[3] != ' ':
        return True
    elif board[1] == board[5] == board[9] and board[1] != ' ':
        return True
    elif board[7] == board[5] == board[3] and board[7] != ' ':
        return True
    else:
        return False


def ifdraw():
    if board.count(' ') < 2:
        return True
    else:
        return False


def is_available(pos):
    return True if board[pos] == ' ' else False


def insert(letter, pos):
    if is_available(pos):
        board[pos] = letter
        disp_board(board)
        if check():
            if letter == 'X':
                print("Computer Wins")
                exit()
            else:
                print("Human wins")
                exit()
        if ifdraw():
            print("Draw")
            exit()
    else:
        if letter == 'O':
            pos = int(input("Not Free! Please re-enter a position"))
        else:
            pos = random.randint(1, 9)
        insert(letter, pos)


def human_move(letter):
    pos = int(input("Enter the position to insert:"))
    insert(letter, pos)


def comp_move(letter):
    pos = random.randint(1, 9)
    insert(letter, pos)


while not check():
    disp_board(board)
    comp_move(computer)
    human_move(human)
    