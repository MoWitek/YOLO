
class colors:
    red = "\033[91m"
    green = "\033[92m"
    yellow = "\033[93m"
    pink = "\033[95m"
    clear = "\033[0m"






class Board:
    def __init__(self):
        self._arr = [[]]

    def expand_top(self, y):
        pass

    def enpand_bot(self, y):
        now = len(self._arr[0])
        dif = x - now + 1

        for n in range(dif):
	    

    def expand_lefts(self, x):
        pass

    def expand_right(self, x):
        now = len(self._arr)
        dif = x - now + 1

        for n in range(dif):
            self._arr.append([dict() for y in range(len(self._arr[0]))])

if __name__ == "__main__":
    b = Board()
    b.expand_right(2)

    print(b._arr)




