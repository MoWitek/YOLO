from __future__ import annotations
from typing import List, Dict, Tuple


data = [[tuple(x.split(" ")) for x in s.split("\n")] for s in

"""4 1
3 2
5 2
5 1

3 1
4 1
3 2
4 2
4 3
2 1

5 8
7 2
8 7
3 5
7 4
1 8
1 5
3 8
5 4
3 4
4 2
6 5
1 6
1 2
6 8

7 4
7 6
4 10
5 9
3 2
1 10
1 6
7 10
4 9
6 10
2 9
1 4
5 1
5 8
2 8
7 3
6 9
6 8
5 4
7 9

20 6
15 7
10 3
5 3
8 18
5 16
9 12
3 9
20 4
9 7
3 1
12 11
6 2
2 11
19 6
17 1
5 7
3 6
9 17
19 3
5 18
20 13
20 11
14 12
14 15
4 1
20 2
20 17
14 20
14 9
16 11
5 1
5 11
3 17
8 17
17 6
20 19
8 13
13 9
20 10
17 11
8 3
7 2
14 13
16 2
5 2
20 12
8 1
9 6
8 11
5 19
17 2
13 11
20 3
14 19
19 11
10 2
16 13
5 15
14 17
5 20
14 6
8 2
5 14
15 2
20 7
3 7
10 9
14 4
15 11
8 7
7 1
9 18
10 11
4 18
7 6
13 17
16 9
10 18
8 9
9 11
15 18
9 4
2 1
8 19
16 15
8 16
5 10
10 6
16 4
18 1
19 12
5 4
13 7
3 2
4 2
6 11
7 11
15 9
19 10
12 1
10 15
14 1
19 7
17 18
19 18
4 6
14 18
10 4
10 12
20 1
18 2
20 18
15 3
8 14
3 12
3 11
13 12
16 18
15 12
8 12
2 12
5 17
19 1
19 2
6 18
4 17
8 20
5 12
15 6
16 12
18 11
14 7
15 4
16 3
20 9
16 7
18 12
6 12
14 10
20 16
10 1
6 1
16 17
15 1
13 4
8 4
5 8
5 13
3 4""".split("\n\n")]


def count(arr):
    counts = {}
    for x in arr:
        counts[x] = counts.get(x, 0) + 1
    return counts


def main():
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
    
    if true_king:
        print(id, "IS THE HEVIEST, mf")
    else:
        print("no true king")



if __name__ == "__main__":
    main()

