board = [[' ' for _ in range(3)] for _ in range(3)]

def display_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 9)

def player_input(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter column (0-2): "))

            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("Spot already taken, pick another spot.")
        except:
            print("Error, Please enter numbers between 0 and 2!")


def check_win(player):
    for row in board:
        if row.count(player) == 3:
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def play():
    current_player = 'X'
    while True:
        display_board(board)
        player_input(current_player)

        if check_win(current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

play()