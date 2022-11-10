from numero_dos import make_board, print_board


b = make_board(8, 10, default_value=0)


def draw_crystal(x, y, it, board):
	b = board

	b[y][x] = "0"
	
	# ->
	for n in range(it):
		if x + n + 1 <= len(board[0]):
			b[y][x + n + 1] = it
		# |\
		#  -
		for n2 in range(it - 1):
			b[y + n2 + 1][x + n + 1] = it

	# <-
	for n in range(it):
		if x - n - 1 >= 0:
			b[y][x - n - 1] = it
	
	# |
	#\ /
	for n in range(it):
		if y + n + 1 <= len(board):
			b[y + n + 1][x] = it

	#/ \
	# |
	for n in range(it):
		if y - n - 1 >= 0:
			b[y - n - 1][x] = it


print_board(b)
print()
# b[3][1] = "AAAA"

draw_crystal(1, 3, 3, b)

print_board(b)




