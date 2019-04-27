from prettytable import PrettyTable

board_definition = []
for i in range(1, 8, 3):
	board_definition.append(list(range(i, i + 3)))

current_board = [[''] * 3] * 3
players = ['Player_1', 'Player_2']
player_symbols = {'Player_1': 'X', 'Player_2': 'O'}
current_player = 'Player_1'
valid_moves = set(range(1, 10))
move_lookup = {1: (0,0), 2: (0,1), 3: (0,2), 4: (1,0), 5: (1,1), 6: (1,2), 7: (2,0), 8: (2,1), 9: (2,2)}
moves = {'Player_1': set(), 'Player_2': set()}
used_moves = set()
winning_sets = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
winner = ''
done = False

def prettify_board(ugly_board):
	pretty_board = PrettyTable()
	pretty_board.header = False
	pretty_board.hrules = True
	for row in ugly_board:
		pretty_board.add_row(row)
	return pretty_board

print('Welcome to tic-tac-toe!')
print("Player_1 is '%s' and Player_2 is '%s'." % (player_symbols['Player_1'], player_symbols['Player_2']))
print('Below is your board.')
print(prettify_board(board_definition))
print('Please take turns by typing the number corresponding to the space you want.')

while not done:
	move = int(input(current_player + '\'s move: '))
	while move in used_moves or move not in valid_moves:
		if move not in valid_moves:
			move = int(input('That is not a valid move. Please select an integer from 1 to 9. '))
		elif move in used_moves:
			move = int(input('That move is already taken. Please make a different move. '))
	used_moves = used_moves.union({move})
	moves[current_player] = moves[current_player].union({move})
	current_board[move_lookup[move][0]][move_lookup[move][1]] = player_symbols[current_player]
	print('Below is the current board:')
	print(prettify_board(current_board))
	for winning_set in winning_sets:
		if len(moves[current_player].intersection(winning_set)) == 3:
			winner = current_player
			print(winner + ' wins!  Thank you for playing!')
			done = True
			break
	current_player = [player for player in players if player != current_player][0]
	if len(used_moves) == 9 and winner == '':
		print('It\'s a tie!  Thank you for playing!')
		done = True
