def make_board(x, y, *, default_value = None):
   return [
   		[
			default_value for _ in range(x)
		] for _ in range(y)
	]

def print_board(board):
	for y in range(len(board)):
		for x in range(len(board[0])):
			print(board[y][x], end=" ")
		print()

class CrystalMeth:
	def __init__(self, board_ref: list, pos: tuple):
		self.board = board_refa
		self.x, self.y = pos
    
		self._cycles = 0

	def grow():
		# mark center
		board[x][y] = "x"

		for n1 in range(self._cycles):
			for n2 in range(self._cycles):
				if n1 - n2:
					pass 
	

print(make_board(2, 5))
print_board(make_board(2, 5))


