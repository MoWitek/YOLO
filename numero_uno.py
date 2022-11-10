def main():
    alice = "./stuff/Aufgabe1/Alice_im_Wunderland.txt"

    with open(alice, "rb") as f:
        content = f.read().decode("utf-8").lower()


    blacklist = "»«,.!?;:\"'&*()-_¹¶[]=\n"
    for b in blacklist:
        content = content.replace(b, " ")

    words = content.split(" ")
    words = list(filter(" ".__ne__, words))


    def rec_starter(patterns: list):
        inxs = [i for i, v in enumerate(words) if v == patterns[0]]

        possibilities = [(words[inx: inx + len(patterns)]) for inx in inxs]

        for p in possibilities:
            for pos_part, pat_part in zip(p, patterns):
                if pat_part == "_":
                    continue

                if pat_part != pos_part:
                    break
            else:
                return p


    dingse = [
        "das _ mir _ _ _ vor",
        "ich muß _ clara _",
        "fressen _ gern _",
        "das _ fing _",
        "ein _ _ tag",
        "wollen _ so _ sein"
    ]
    y = []
    for dings in dingse:
        x = rec_starter(dings.split(" "))
        y.append(x is not None)

    return y

if __name__ == '__main__':
    main()