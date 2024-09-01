import random
import math


# Function to check the maximum sum of any winning line (row, column, or diagonal)
def check_best_line_sum(board):
    # Define the winning combinations (rows, columns, diagonals)
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]

    max_sum = -math.inf  # Initialize the maximum sum to negative infinity

    # Iterate over each winning combination
    for combination in winning_combinations:
        # Calculate the sum of the current combination
        line_sum = sum(board[i] for i in combination if board[i] is not None)
        # Update the maximum sum if the current line sum is greater
        max_sum = max(max_sum, line_sum)

    return max_sum  # Return the maximum sum found


# Function to check for available moves on the board
def available_moves(board):
    # Return a list of indices where the board has empty spots (None)
    return [i for i, spot in enumerate(board) if spot is None]


# Main MinMax algorithm function
def minimax(board, depth, is_maximizing):
    # Base case: If no moves are left, return the best line sum
    if not available_moves(board):
        return check_best_line_sum(board)

    # If it's the maximizing player's turn
    if is_maximizing:
        best_score = -math.inf  # Initialize the best score to negative infinity

        # Loop over all available moves
        for move in available_moves(board):
            board[move] = random.randint(0, 9)  # Place a random number (0-9) on the board
            score = minimax(board, depth + 1, False)  # Recursively call minimax for the minimizing player
            board[move] = None  # Undo the move
            best_score = max(score, best_score)  # Update the best score

        return best_score  # Return the best score found

    # If it's the minimizing player's turn
    else:
        best_score = math.inf  # Initialize the best score to positive infinity

        # Loop over all available moves
        for move in available_moves(board):
            board[move] = random.randint(0, 9)  # Place a random number (0-9) on the board
            score = minimax(board, depth + 1, True)  # Recursively call minimax for the maximizing player
            board[move] = None  # Undo the move
            best_score = min(score, best_score)  # Update the best score

        return best_score  # Return the best score found


# Function to find the best move for the maximizing player
def best_move(board):
    best_score = -math.inf  # Initialize the best score to negative infinity
    move = None  # Initialize the best move as None

    # Loop over all available moves
    for i in available_moves(board):
        board[i] = random.randint(0, 9)  # Place a random number (0-9) on the board
        score = minimax(board, 0, False)  # Evaluate this move using MinMax
        board[i] = None  # Undo the move

        # If the current move's score is better, update the best score and move
        if score > best_score:
            best_score = score
            move = i

    return move  # Return the best move found


# Example usage:
# Initial board (None represents an empty space)
board = [None, None, None,
         None, None, None,
         None, None, None]

# Find the best move for maximizing the sum
best_move_position = best_move(board)
print(f"The best move is at position: {best_move_position}")