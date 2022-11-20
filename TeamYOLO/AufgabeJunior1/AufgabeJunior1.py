from dataset import JuniorAufgabe1 as Aufgabe

# if char or str is only made up of vocals
def has_voc(str):
    for l in str:
        if l not in "aeiouöäü":  # öüä -> CRINGE
            return False
    return True

# taifun  -> t  ai f u n
# aaabbbcdefg -> aaa bbbcd e fg
# split up onto vocs and kons
def get_vokalgrupe(word):
    syl = word[0]
    sylables = []
    last = not has_voc(syl)
    for l in word[1:]:
        if has_voc(l) is last:
            sylables.append(syl)
            syl = ""
            last = not last
        syl += l
    sylables.append(syl)

    return sylables

def vocals(word):
    syl1 = get_vokalgrupe(word)

    if not has_voc(syl1[0]):
        syl1.pop(0)
    syl1 = list(filter(has_voc, syl1))

    return syl1


# get vocgruppe of both, check if following part is same
def regel1(w1: str, w2: str):
    def get_last_same(word):
        syl1 = get_vokalgrupe(word)

        buff = ""
        br = 0
        for sr in syl1[::-1]:
            buff += sr[::-1]
            if has_voc(sr):
                br += 1
                if br == (1 if len(vocals(word)) == 1 else 2):
                    break

        return buff[::-1]

    v1, v2 = get_last_same(w1), get_last_same(w2)

    return v1 == v2


# voc gruppe + following part >= 50% of word
def regel2(w1: str, w2: str):

    # check if the words following part is bigger than 50%
    def bigger_than_half(word):
        syl1 = get_vokalgrupe(word)

        buff = ""
        for l in syl1[::-1][:(1 if len(vocals(word)) == 1 else 2) * 2]:
            buff += l

        return not ((len(buff) / len(word)) < .5)

    return not (not bigger_than_half(w1) or not bigger_than_half(w2))


# word 1 cant end with word 2 and otherwise
def regel3(w1: str, w2: str):
    return not w1.endswith(w2) or w2.endswith(w1)


def regel123(w1: str, w2: str):
    return regel1(w1, w2), regel2(w1, w2), regel3(w1, w2)

# match pairs
def sorter(words: list):
    pairs = []
    lost = []
    try:
        # get the first word
        for n in range(len(words) - 1):
            w1 = words.pop()
            # iterate over all other words
            for i, w2 in enumerate(words):
                if regel1(w1, w2) and regel2(w1, w2) and regel3(w1, w2):
                    # if one word matches, save words and remove w1 from the pool
                    pairs.append((w1, w2))
                    words.pop(i)
                    break
            # if none match
            else:
                lost.append(w1)

    finally:
        return pairs, lost

def nice_print(ls, lost):
    srs = []
    for x, y in ls:
        srs.append(f"{x} + {y}")

    return ", ".join(srs) + "\n" + ", ".join(lost)

def match_rhymes(data: str = Aufgabe.txt0):
    words = data.lower().split("\n")

    return sorter(words)


if __name__ == "__main__":
    txt = Aufgabe.txt1
    # print(match_rhymes(txt))
    print(nice_print(*match_rhymes(txt)))

    # print(regel123("schwank", "schlank"))
