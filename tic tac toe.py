def print_board(board):
    print()
    for i in range(3):
        print(" ", board[3*i], "|", board[3*i+1], "|", board[3*i+2])
        if i < 2:
            print(" ---|---|---")
    print()

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for cell in board)

def tic_tac_toe():
    board = [str(i+1) for i in range(9)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!\nPlayer 1 is 'X' and Player 2 is 'O'")
    print_board(board)
    while True:
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] in ['X', 'O']:
                print("That spot is already taken. Try again.")
                continue
            board[move] = current_player
            print_board(board)

            if check_win(board, current_player):
                print(f"🎉 Player {current_player} wins!")
                break
            elif is_draw(board):
                print("It's a draw!")
                break

            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'
        except (ValueError, IndexError):
            print("Invalid move! Please enter a number from 1 to 9.")

# Run the game
tic_tac_toe()
          
