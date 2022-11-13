from datasets import NormalAufgabe1

def main():
    alice = "./stuff/Aufgabe1/Alice_im_Wunderland.txt"

    with open(alice, "rb") as f:
        content = f.read().decode("utf-8").lower()


    blacklist = "»«,.!?;:\"'&*()-_¹¶[]="
    for b in blacklist:
        content = content.replace(b, " ")
    content.replace("\n", " ")
    content.replace("  ", " ")


    words = content.split(" ")
    words = list(filter(" ".__ne__, words))


    def rec_starter(patterns: list):
        inxs = [i for i, v in enumerate(words) if v == patterns[0]]

        possibilities = [(words[inx: inx + len(patterns)]) for inx in inxs]

        ps = []
        for p in possibilities:
            for pos_part, pat_part in zip(p, patterns):
                if pat_part == "_":
                    continue

                if pat_part != pos_part:
                    break
            else:
                ps.append(p)
        return ps


    dingse = [
        getattr(NormalAufgabe1, atr) for atr in [f"txt{n}" for n in range(6)]
    ]
    y = []
    for dings in dingse:
        x = rec_starter(dings.split(" "))
        y.append(x != [])
        print(f"Phrases matching | {dings} |")
        print("\n".join([" ".join(z) for z in x]))
        print()

    assert list(set(y)) == [True]

    return y

if __name__ == '__main__':
    main()