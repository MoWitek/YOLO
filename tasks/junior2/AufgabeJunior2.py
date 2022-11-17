from __future__ import annotations
from typing import List, Dict
from datasets import JuniorAufgabe2


def solve_for_biggest(data: str = JuniorAufgabe2.txt4, *, null_value=None):
    data = [tuple(x.split(" ")) for x in data.split("\n")]

    # convert the array to a kinda binary tree
    # 2 -> 1
    # 3 -> 2
    vs: Dict[str, List[str]] = {}
    for x, y in data:
        if x not in vs:
            vs[x] = []
        vs[x].append(y)

    # traverse binary tree
    # follow all the paths and save them
    # 2 -> 1
    # 3 -> 2 -> 1
    def rec(values, chain):
        if values is None:
            return
        for vl in values:
            F = vs.get(vl)
            chain.add(vl)
            rec(F, chain)


    # get all chains
    # 1
    # 2 1
    true_king = True
    chains = []
    for k, v in vs.items():
        chain = set()  # chain as set since we done care about duplicate options
        try:
            rec(v, chain)
        except RecursionError:  # prevent looping, 1 -> 2 | 2 -> 1
            true_king = False
        chains.append((k, chain))

    if true_king:
        # get the longest chain
        srted = sorted(chains, key=lambda a: len(a[1]), reverse=True)

        # check there are no multiple highest, bc if there is another option it will not show in the main tree
        id, mx = srted.pop(0)
        for x, y in srted:
            if x not in mx:  # <- this prevents that
                true_king = False
    else:
        id = None

    return id if true_king else null_value

if __name__ == "__main__":
    print([solve_for_biggest(d) for d in [
        JuniorAufgabe2.txt0,
        JuniorAufgabe2.txt1,
        JuniorAufgabe2.txt2,
        JuniorAufgabe2.txt3,
        JuniorAufgabe2.txt4
    ]])

