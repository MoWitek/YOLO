class bcolors:
    blu = '\033[94m'
    cian = '\033[96m'
    gren = '\033[95m'
    jelou = '\033[93m'


# print(bcolors.jelou + "hi")

for n in range(256):
    print(f"{n} -> \033[{n}m CRINGE")

