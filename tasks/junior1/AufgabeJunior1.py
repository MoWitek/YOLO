from datasets import JuniorAufgabe1 as Aufgabe


def has_voc(str):
    for l in str:
        if l not in "aeiouöäü":  # öüä -> CRINGE
            return False
    return True

# taifun  -> t  ai f u n
# aaabbbcdefg -> aaa bbbcd e fg
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


def regel1(w1: str, w2: str):
    def get_last_same(word):
        syl1 = get_vokalgrupe(word)

        if not has_voc(syl1[0]):
            syl1.pop(0)

        buff = ""
        br = 0
        for sr in syl1[::-1]:
            buff += sr[::-1]
            if has_voc(sr):
                br += 1
                if br == 2:
                    break

        return buff[::-1]

    v1, v2 = get_last_same(w1), get_last_same(w2)

    return v1 == v2


def regel2(w1: str, w2: str):
    def vocals(word):
        syl1 = get_vokalgrupe(word)

        if not has_voc(syl1[0]):
            syl1.pop(0)
        syl1 = list(filter(has_voc, syl1))

        return syl1

    v1, v2 = vocals(w1), vocals(w2)


    if (v1[(-2) if len(v1) > 1 else -1]) != (v2[(-2) if len(v2) > 1 else -1]):
        return False

    def fn(word):
        syl1 = get_vokalgrupe(word)

        buff = ""
        for l in syl1[::-1][:4]:
            buff += l

        return not len(buff) / len(word) < .5

    return not (not fn(w1) or not fn(w2))


def regel3(w1: str, w2: str):
    return not w1.endswith(w2) or w2.endswith(w1)


def regel123(w1: str, w2: str):
    return regel1(w1, w2), regel2(w1, w2), regel3(w1, w2)


def sorter(words: list):
    pairs = []
    lost = []
    try:
        for n in range(len(words) - 1):
            w1 = words.pop()
            for i, w2 in enumerate(words):
                if regel1(w1, w2) and regel2(w1, w2) and regel3(w1, w2):
                    pairs.append((w1, w2))
                    words.pop(i)
                    break
            else:
                lost.append(w1)

    finally:
        return pairs, lost


def match_rhymes(data: str = Aufgabe.txt3):
    words = data.lower().split("\n")

    return sorter(words)


if __name__ == "__main__":
    print(match_rhymes(Aufgabe.txt2))

    print(regel123("konsumption", "absorption"))
