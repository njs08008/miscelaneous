"""
This is a Python implementation of the classic game Minesweeper.
It is currently a work in progress, and is nowhere near done.
"""

from prettytable import PrettyTable
import random

# Collect user input for board setup
while True:
	try:
		board_width = int(input('Please enter the board width as an integer between 1 and 20. '))
		if board_width >= 1 and board_width <= 20:
			break
		else:
			print('The board width must be between 1 and 20.')
	except:
		print('Please enter an integer.')

while True:
	try:
		board_height = int(input('Please enter the board height as an integer between 1 and 20. '))
		if board_height >= 1 and board_height <= 20:
			break
		else:
			print('The board height must be between 1 and 20.')
	except:
		print('Please enter an integer.')

n_tiles = board_width * board_height
print(n_tiles)

while True:
	try:
		n_mines = int(input('Please enter the number of mines as an integer between 1 and %i. ' % n_tiles))
		if n_mines >= 1 and n_mines <= n_tiles:
			break
		else:
			print('The number of mines must be between 1 and %i' % n_tiles)
	except:
			print('Please enter an integer.')

# Create the board
true_board = [0] * n_tiles
mines = random.sample(range(n_tiles), n_mines)
for mine in mines:
	true_board[mine] = 1

def prettify_board(ugly_board):
	pretty_board = PrettyTable()
	pretty_board.header = False
	pretty_board.hrules = True
	for row in ugly_board:
		pretty_board.add_row(row)
	return pretty_board

shown_board = [[''] * board_width] * board_height

while True:
	print('Below is your current board.')
	print(prettify_board(shown_board))


