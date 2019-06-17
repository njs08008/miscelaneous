"""
This defines a class for a tic-tac-toe game.
"""

from itertools import cycle
from random import choice

class tic_tac_toe:
	"""A game of tic-tac-toe between two players, human or computer."""
	def __init__(self, n_humans = 2):
		self.board = [['-' for i in range(3)] for i in range(3)]

		self.n_humans = n_humans

		self.symbols = ['X', 'O']
		self.symbols_cycle = cycle([self.symbols[0], self.symbols[1]])
		self.current_symbol = next(self.symbols_cycle)

		self.player_type_dict = {2: ['human', 'human'], 1: ['human', 'computer'], 0: ['computer', 'computer']}
		self.player_types = cycle(self.player_type_dict[n_humans])
		self.current_player_type = next(self.player_types)

		self.move_lookup = move_lookup = {1: (0,0), 2: (0,1), 3: (0,2), 4: (1,0), 5: (1,1), 6: (1,2), 7: (2,0), 8: (2,1), 9: (2,2)}
		self.winning_move_sets = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
		self.player_moves = {self.symbols[0]: set(), self.symbols[1]: set()}

		self.has_winner = False

	def print_board_definition(self):
		"""Prints what spaces correspond to what move on the board."""
		for i in range(3):
			row = []
			for j in range(3):
				row.append(str(3*i + j+1))
			print('|'.join(row))
		print('')

	def print_board(self):
		"""Prints the current state of the board."""
		for row in self.board:
			print('|'.join(row))
		print('')

	def winning_player(self, symbol):
		"""Determine if someone has won."""
		if symbol not in self.symbols:
			raise Exception('Invalid player symbol provided.')
		return any([len(winning_move_set.intersection(self.player_moves[symbol])) == 3 for winning_move_set in self.winning_move_sets])

	def board_full(self):
		"""Returns a boolean for whether or not the board is full."""
		full = True
		for row in self.board:
			if '-' in row:
				full = False
				break
		return full

	def validate_move(self, move):
		"""Return boolean for whether provided move is valid."""
		return move in range(1, 10)

	def use_move(self, move, symbol):
		"""Add the move to the set of moves the player has used."""
		if symbol not in self.symbols:
			raise Exception('Invalid player symbol provided.')
		self.player_moves[symbol] = self.player_moves[symbol].union([move])

	def add_token(self, move, symbol):
		"""Accepts a move and an arbitrary symbol."""
		if not self.validate_move(move):
			raise Exception('Invalid move provided.')
		if self.board_full():
			raise Exception('There are no remaining moves.')
		elif self.board[self.move_lookup[move][0]][self.move_lookup[move][1]] != '-':
			raise Exception('That move is already taken.')
		else:
			self.use_move(move, symbol)
			self.board[self.move_lookup[move][0]][self.move_lookup[move][1]] = symbol

	def computer_move(self, symbol):
		"""Make a random move for the computer."""
		if self.board_full():
			raise Exception('There are no remaining moves.')
		else:
			used_moves = [move for moves in self.player_moves.values() for move in moves]
			available_moves = [move for move in range(1, 10) if move not in used_moves]
			move = choice(available_moves)
			self.add_token(move, symbol)

	def human_move(self, move, symbol):
		"""Allow a human player to make a move."""
		self.add_token(move, symbol)

	def alternate_player(self):
		"""Change whose turn it is."""
		self.current_symbol = next(self.symbols_cycle)
		self.current_player_type = next(self.player_types)

	def play_game(self):
		"""Play a game!"""
		print('Welcome to tic-tac-toe! Below is your board definition. Enter the number corresponding to the spot you want when asked.\n')
		self.print_board_definition()
		while not self.board_full():
			print('Player %s\'s turn.' % self.current_symbol)
			if self.current_player_type == 'human':
				move = int(input('Please enter your move: '))
				self.human_move(move, self.current_symbol)
			else:
				self.computer_move(self.current_symbol)
			self.print_board()
			if self.winning_player(self.current_symbol):
				self.has_winner = True
				print('Player %s wins!' % self.current_symbol)
				break
			self.alternate_player()
		if not self.has_winner:
			print('It\'s a tie!')

def play_ttt_vs_computer():
	"""Automatically play human vs. computer when this script is run."""
	ttt = tic_tac_toe(n_humans=1)
	ttt.play_game()

if __name__ == '__main__':
	play_ttt_vs_computer()
