from datasets import NormalAufgabe1

def preprocess_data(string: str):
    string = string.lower()

    oks = "abcdefghijklmnopqrstuvwxyzöäüß"

    blacklist = set(string) - set(oks)

    for b in blacklist:
        string = string.replace(b, " ")

    string = string.replace("\n", " ").replace("  ", " ")

    words = string.split(" ")
    words = list(filter(" ".__ne__, words))
    words = list(filter("".__ne__, words))

    return words

def searcher(words, pattern: str):
    pattern = pattern.split(" ")

    inxs = [i for i, v in enumerate(words) if v == pattern[0]]  # get all positions of first word, since its always known

    possibilities = [(words[inx: inx + len(pattern)]) for inx in inxs]  # get the first word and a few words after it

    ps = []
    for p in possibilities:
        for pos_part, pat_part in zip(p, pattern):
            if pat_part == "_":
                continue

            if pat_part != pos_part:
                break
        else:
            ps.append(p)

    return ps


def regex_search(pattern, text: str = NormalAufgabe1.alice):

    words = preprocess_data(text)

    return searcher(words, pattern)

if __name__ == '__main__':
    pat = NormalAufgabe1.txt5
    print(pat)
    print(regex_search(pat))
