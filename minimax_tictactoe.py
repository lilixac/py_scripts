# Initialize the board as 2D array
board = [
	['-','-','-'],
	['-','-','-'],
	['-','-','-']
]

# set x as AI and o as player
ai = 'x'
player = 'o'


def print_board(board):
	'''
	Prints the board in proper format.
	'''
	for i in board:
		print(i[0], '|', i[1], '|', i[2])
		print('-- --- --')

def winner(board):
	'''
	Returns the game state.
	Checks if player won, AI won, game is tied or game not over yet.

	:param board: Current snapshot of the board array
	'''

	# horizontal win
	for i in range(3):
		if board[i][0] == board[i][1] == board[i][2] != "-":
			return board[i][0]

	# vertical win
	for i in range(3):
		if board[0][i] == board[1][i] == board[2][i] != "-":
			return board[0][i]			

	# diagonal win
	if board[0][0] == board[1][1] == board[2][2] != "-":
		return board[0][0]

	if board[0][2] == board[1][1] == board[2][0] != "-":
		return board[0][2]

	# check if board is full
	for i in board:
		for j in i:
			if j == "-":
				return "not over"

	return "tie"

def fill(board, i, j, turn_of):
	'''
	Fills the board at the specified position.
	If player tries to fill at the position which is already occupied, thie method is called again.

	:param board: Current snapshot of the board array.
	:param i: First index for the position of the board to be filled.
	:param j: Second index for the position of the board to be filled.
	:param turn_of: Turn of player or AI. 
	'''
	i = int(i)
	j = int(j)
	if board[i][j] == "-":
		board[i][j] = turn_of
	elif board[i][j] == "x" or "o":
		print("Already Filled.")
		move = input("Enter the move position again, [i,j]:\t")
		i,j = move.split(',')
		fill(board, i, j, turn_of)

def minimax(board, is_maximizing):
	'''
	Implementation of Minimax Algorithm.

	:param board: Current snapshot of the board array.
	:is_mazimizing: Check if it is turn of maximizing player or minimizing player.

	returns bestScore
	'''

	# If current board is a terminal state.
	if winner(board) == "x":
		return 1
	elif winner(board) == "o":
		return -1
	elif winner(board) == "tie":
		return 0

	# Move for maximizing player (AI)
	if is_maximizing:
		best_score = -2
		for i in range(3):
			for j in range(3):
				if board[i][j] == "-":
					board[i][j] = ai
					score = minimax(board, False)
					board[i][j] = "-"
					best_score = max(score, best_score)
		return best_score
	# Move for minimizing player (Player)
	else:
		best_score = 2
		for i in range(3):
			for j in range(3):
				if board[i][j] == "-":
					board[i][j] = player
					score = minimax(board, True)
					board[i][j] = "-"
					best_score = min(score, best_score)
		return best_score

def best_move(board):
	'''
	Returns the best possible position for AI.

	:param board: Current snapshot of the board array.
	'''
	best_score = -2
	a = -1
	b = -1
	for i in range(len(board)):
		for j in range(len(board[0])):
			if (board[i][j] == "-"):
				board[i][j] = ai
				score = minimax(board, False) # AI is maximizing, next move will be of player, so check optimality
				board[i][j] = "-"
				if score > best_score:
					best_score = score
					a = i
					b = j
	return a, b

def game(board):	
	'''
	Game logic
	'''
	
	# 0 is player, 1 is AI
	turn_of = 0 

	# Continues till the game is not over.
	while (winner(board) == "not over"):
		print_board(board)
		if turn_of == 0:  ## Player's turn at first.
			print("Your turn:")
			move = input("Enter the move position, [i,j]:\t")
			i,j = move.split(',')
			fill(board, i, j, player)
			turn_of = (turn_of + 1) % 2
		else:
			print("AI's turn:") ## AI's turn.
			i,j = best_move(board)
			fill(board, i, j, ai)
			turn_of = (turn_of + 1) % 2

		## Prints the final result of  the game
		if winner(board) == 'x':
			print_board(board)
			print("AI is the winner")
		elif winner(board) == "o":
			print_board(board)
			print("Player is the winner")
		elif winner(board) == "tie":
			print_board(board)
			print("Tie")

if __name__ == '__main__':
	game(board)