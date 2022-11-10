alice = "cringelig"


with open(alice, "rb") as datei:
    inhalt: str = datei.read().decode("utf-8").lower()

# satzzeichen wegstreichen um genauigkeit zu maximieren
for b in "»«,.!?;:\"'&*()-_¹¶[]=\n":
    inhalt = inhalt.replace(b, " ")

woerter = inhalt.split(" ")
woerter = list(filter(" ".__ne__, woerter))


def text_suche(muster: list):
    # jede position vom ersten wort im muster
    positionen = []
    for position, wert in enumerate(woerter):
        if wert == muster[0]:
            positionen.append(position)

    # positionen = [i for i, v in enumerate(woerter) if v == muster[0]]

    #
    moeglichkeiten = []
    for position in positionen:
        moeglichkeiten.append(woerter[position : position + len(muster)])

    # moeglichkeiten = [woerter[position: position + len(muster)] for position in positionen]

    for m in moeglichkeiten:
        for position_teil, muster_teil in zip(m, muster):
            if muster_teil == "_":
                continue

            if muster_teil != position_teil:
                break
        else:
            return m


ergebnisse = []
for t in [
    "das _ mir _ _ _ vor",
    "ich muß _ clara _",
    "fressen _ gern _",
    "das _ fing _",
    "ein _ _ tag",
    "wollen _ so _ sein"
]:
    x = text_suche(t.split(" "))
    ergebnisse.append(x is not None)

print(ergebnisse)