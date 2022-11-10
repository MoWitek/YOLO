from __future__ import annotations
from typing import List, Dict
from datasets import JuniorAufgabe2


def solve_for_biggest(data: str = JuniorAufgabe2.txt4):
    data = [tuple(x.split(" ")) for x in data.split("\n")]

    vs: Dict[str, List[str]] = {}
    for x, y in data:
        if x not in vs:
            vs[x] = []
        vs[x].append(y)


    def rec(values, chain):
        if values is None:
            return
        for vl in values:
            F = vs.get(vl)
            chain.add(vl)
            rec(F, chain)


    true_king = True
    chains = []
    for k, v in vs.items():
        chain = set()
        try:
            rec(v, chain)
        except RecursionError:
            true_king = False
        chains.append((k, chain))


    if true_king:
        srted = sorted(chains, key=lambda a: len(a[1]), reverse=True)
        id, mx = srted.pop(0)
        for x, y in srted:
            if x not in mx:
                true_king = False
    else:
        id = None

    return id if true_king else None

if __name__ == "__main__":
    print([solve_for_biggest(d) for d in [
        JuniorAufgabe2.txt0,
        JuniorAufgabe2.txt1,
        JuniorAufgabe2.txt2,
        JuniorAufgabe2.txt3,
        JuniorAufgabe2.txt4
    ]])

