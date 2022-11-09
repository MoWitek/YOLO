def create_slope(sz, fill, back):
	ar=[]
	for n in range(sz):
		a2 = []
		a2.extend([fill for n in range(n + 1)])
		a2.extend([back for n in range(sz - n - 1)])
		ar.append(a2)

	return ar

def print_board(board):
	for y in range(len(board)):
		for x in range(len(board[0])):
			print(board[y][x], end=" ")
		print()

def fuze_slopes(s, fill=1, back=0):
	rotate = lambda arr: [ list(x) for x in list(zip(*arr[::-1]))]

	a1 = create_slope(s, fill, back)
	a2 = rotate(create_slope(s, fill, back))
	a3 = rotate(rotate(create_slope(s, fill, back)))
	a4 = rotate(rotate(rotate(create_slope(s, fill, back))))

	arr = []
	for a, b in zip(a4, a1):
		arr.append([])
		arr[-1].extend(a)
		arr[-1].extend(b[1:])
	for c, d in zip(a3[1:], a2[1:]):
		arr.append([])
		arr[-1].extend(c)
		arr[-1].extend(d[1:])

	return arr

	
print_board(fuze_slopes(3))
