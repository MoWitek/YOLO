from __future__ import annotations
from typing import List, Dict
from datasets import JuniorAufgabe2

def count(arr):
    counts = {}
    for x in arr:
        counts[x] = counts.get(x, 0) + 1
    return counts


def main(data: str = JuniorAufgabe2.txt4):
    data = [[tuple(x.split(" ")) for x in s.split("\n")] for s in data.split("\n")]

    d = data[1]

    vs: Dict[str, List[str]] = {}
    for x, y in d:
        if x not in vs:
            vs[x] = []
        vs[x].append(y)


    def rec(values, chain):
        if values is None:
            return
        for v in values:
            F = vs.get(v)
            chain.add(v)
            rec(F, chain)


    chains = []
    for k, v in vs.items():
        chain = set()
        rec(v, chain)
        chains.append((k, chain))

    srted = sorted(chains, key=lambda a: len(a[1]), reverse=True)
    id, mx = srted.pop(0)
    true_king = True
    for x, y in srted:
        if x not in mx:
            true_king = False
            print("fak", x)

    return id if true_king else None

if __name__ == "__main__":
    main()

