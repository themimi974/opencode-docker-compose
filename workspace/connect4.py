import os

BOARD_ROWS = 6
BOARD_COLS = 7
EMPTY = ' '
PLAYER_1 = 'X'
PLAYER_2 = 'O'

def create_board():
    return [[EMPTY for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n  1   2   3   4   5   6   7")
    print("+" + "---+" * BOARD_COLS)
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+" + "---+" * BOARD_COLS)
    print()

def is_valid_move(board, col):
    return 0 <= col < BOARD_COLS and board[0][col] == EMPTY

def drop_piece(board, col, player):
    for row in range(BOARD_ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = player
            return row
    return -1

def check_winner(board, row, col, player):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    
    for dr, dc in directions:
        count = 1
        
        for d in [1, -1]:
            r, c = row + dr * d, col + dc * d
            while 0 <= r < BOARD_ROWS and 0 <= c < BOARD_COLS and board[r][c] == player:
                count += 1
                r += dr * d
                c += dc * d
        
        if count >= 4:
            return True
    
    return False

def is_board_full(board):
    return all(cell != EMPTY for cell in board[0])

def get_player_input(player):
    while True:
        try:
            col = int(input(f"Player {player}, choose column (1-7): ")) - 1
            return col
        except ValueError:
            print("Please enter a valid number.")

def main():
    board = create_board()
    players = [PLAYER_1, PLAYER_2]
    current_player = 0
    
    while True:
        print_board(board)
        player = players[current_player]
        col = get_player_input(player)
        
        if not is_valid_move(board, col):
            print("Invalid move! Column is full or invalid.")
            continue
        
        row = drop_piece(board, col, player)
        
        if check_winner(board, row, col, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = 1 - current_player

if __name__ == "__main__":
    main()
