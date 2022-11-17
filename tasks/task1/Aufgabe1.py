from datasets import NormalAufgabe1

# make data processavble
def preprocess_data(string: str):
    string = string.lower()

    oks = "abcdefghijklmnopqrstuvwxyzöäüß"  # we only search for words
    blacklist = set(string) - set(oks)
    for b in blacklist:
        string = string.replace(b, " ")


    # filter out empty string parts
    string = string.replace("\n", " ").replace("  ", " ")
    words = string.split(" ")
    words = list(filter(" ".__ne__, words))
    words = list(filter("".__ne__, words))

    return words

def searcher(words, pattern: str):
    pattern = pattern.split(" ")

    while pattern[0] == "_":  # make sure pat[0] is always a word
        pattern.pop(0)

    inxs = [i for i, v in enumerate(words) if v == pattern[0]]  # get all positions of first word, since its always known

    possibilities = [(words[inx: inx + len(pattern)]) for inx in inxs]  # get the first word and a few words after it

    # for each position we check if the following words either match the pattern or can be ignored bc of the pattern
    # if the word does not match the possibility can be discarded
    viable_possibilities = []
    for p in possibilities:
        for pos_part, pat_part in zip(p, pattern):
            if pat_part == "_":  # skip if patten is empty
                continue

            if pat_part != pos_part:  # discard if word does not match pattern
                break
        else:
            viable_possibilities.append(p)  # if patten is ok save possibility as viable

    return viable_possibilities


def regex_search(pattern, text: str = NormalAufgabe1.alice):

    words = preprocess_data(text)

    return searcher(words, pattern)

if __name__ == '__main__':
    pat = "_ " + NormalAufgabe1.txt5
    print(pat)
    print(regex_search(pat))
