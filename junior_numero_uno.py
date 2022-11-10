from datasets import JuniorAufgabe1 as Aufgabe

"""
1) Die beiden Worte enden gleich: Sie haben
dieselbe maßgebliche Vokalgruppe, und nach der
maßgeblichen Vokalgruppe enthalten beide Wörter
dieselben Buchstaben in derselben Reihenfolge.
Dabei ist eine Vokalgruppe eine längstmögliche
Folge von unmittelbar aufeinanderfolgenden
Vokalen (z.B. hat das Wort
Taifun die Vokalgruppen
ai und u), und die maßgebliche Vokalgruppe
eines Wortes ist seine vorletzte Vokalgruppe, wenn
das Wort zwei oder mehr Vokalgruppen enthält.
Enthält ein Wort nur eine Vokalgruppe, ist seine
maßgebliche Vokalgruppe die eine vorhandene
Vokalgruppe.

2) In jedem der beiden Wörter enthält die maß-
gebliche Vokalgruppe und was ihr folgt mindestens
die Hälfte der Buchstaben.

3) Keines der beiden Wörter darf mit dem kom-
pletten anderen Wort enden.

Passende Wortpaare wären zum Beispiel
Baum,Traum und
singen,
klingen; aber
Tanne,
Rinne ver-
letzt Regel 1,
Informatik,
Akrobatik verletzt Regel
2, und
kaufen,
verkaufen verletzt Regel 3.
Wende dein Programm mindestens auf alle
Beispiele an, die du auf den BWINF-Webseit
"""

def is_vok(str):
    for l in str:
        if l not in "aeiouöäü":
            return False
    return True

def get_vokalgruppe(word):
    syl = word[0]
    sylables = []
    last = not is_vok(syl)
    for l in word[1:]:
        if is_vok(l) is last:
            sylables.append(syl)
            syl = ""
            last = not last
        syl += l
    sylables.append(syl)
        
    return sylables

# 
def regel1(w1: str, w2: str):
    def get_last_same(word):
        syl1 = get_vokalgruppe(word)

        if not is_vok(syl1[0]):
            syl1.pop(0)

        # print(syl1)

        buff = ""
        br = 0
        for sr in syl1[::-1]:
            buff += sr[::-1]
            if is_vok(sr):
                br += 1
                if br == 2:
                    break
        buff = buff[::-1]

        return buff

    v1, v2 = get_last_same(w1), get_last_same(w2)


    return v1 == v2
        
    # if (v1[(-2) if len(v1) > 1 else -1]) !=  (v2[(-2) if len(v2) > 1 else -1]):
    #     return False

    # return True

# 
def regel2(w1: str, w2: str):
    # might be useful
    """# selbe maßgebliche vokalgruppe
    def fn(w):
        syl1 = get_vokalgruppe(w)

        if not is_vok(syl1[0]):
           syl1.pop(0) 
        syl1 = list(filter(is_vok, syl1))
            
        mx = []
        prev = syl1[0]
        for s in syl1[1:]:
            if len(prev + s) > len("".join(mx)):
                mx = [prev, s]
        
        return mx

    # letzer
    v1, v2 = fn(w1), fn(w2)
    if v1 != v2:
        return False

    def fn(voc_grp, w):
        pass"""

    def vokale(word):
        syl1 = get_vokalgruppe(word)

        if not is_vok(syl1[0]):
           syl1.pop(0) 
        syl1 = list(filter(is_vok, syl1))
        
        return syl1

    v1, v2 = vokale(w1), vokale(w2)

    #print(v1, v2)
    # letzte vokale gleich
    # print(v1)
    
    if (v1[(-2) if len(v1) > 1 else -1]) !=  (v2[(-2) if len(v2) > 1 else -1]):
        return False
    

    def fn(word):
        syl1 = get_vokalgruppe(word)

        buff = ""
        for l in syl1[::-1][:4]:
            buff+=l

        if len(buff) / len(word) < .5:
            return False

        return True
    
    if not fn(w1):
        return False
     
    if not fn(w2):
        return False
    
    return True



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
                    # print(pairs)
                    # print(w1, w2, words)
                    words.pop(i)
                    break
            else:
                lost.append(w1)

    finally:
        return pairs, lost

def main():
    words = Aufgabe.txt3.lower().split("\n")

    x, y = sorter(words)

    print(x)
    print("\n")
    print(y)
    
if __name__ == "__main__":
    main()
