# Import data
file1 = open('input.txt', 'r')
data = file1.read().split('\n\n')
draws = data[0].split(',')
boards_data = data[1:6]

# Format boards as arrays
boards = []
for b in boards_data:
	board = []
	for row in b.split('\n'):
		board.append([x for x in row.split(' ') if x!=''])
	boards.append(board)

# Helper functions
def display_boards(boards):
	for b in boards:
		for row in b:
			print(('\t').join(row))
		print('\n\n')

def check_for_winners(boards):
	winners = []
	for b in boards:
		# Check rows
		for row in b:
			if row == ['X', 'X', 'X', 'X', 'X']:
				winners.append(b)
		# Check columns
		for i in range(5):
			if 'X' == b[0][i] == b[1][i] == b[2][i] == b[3][i] == b[4][i]:
				winners.append(b)
	return winners

def mark_board(board, draw):
	for i in range(5):
		for j in range(5):
			if board[i][j] == draw:
				board[i][j] = 'X'
	return board

def calculate_result(board):
	s = 0
	for row in board:
		s += sum([int(n) for n in row if n!='X'])
	return s


# Start game
display_boards(boards)

for draw in draws:
	print('NUMBER CALLED:{}'.format(draw))

	boards = [mark_board(board, draw) for board in boards]
	display_boards(boards)
	winners = check_for_winners(boards)

	if len(winners)>0:
		print('WE HAVE A WINNER!!!')
		display_boards(winners)
		print(calculate_result(winners[0]) * int(draw))
		break