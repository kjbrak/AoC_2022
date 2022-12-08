data = open('day8/in8', 'r').read().split('\n')

def create_tree_neighbours(idx:tuple) -> tuple:
    y, x = idx
    yu  = reversed(''.join([s[x] for s in data[:y]]))
    yd  = ''.join([s[x] for s in data[y+1:]])
    xl  = reversed(data[y][:x])
    xr  = data[y][x+1:]
    return (yu, yd, xl, xr)


def is_visible(idx:tuple) -> bool:
    y, x = idx
    t = data[y][x]
    tup = create_tree_neighbours(idx)
    # for lst in (yu, yd, xl, xr):
    for s in tup:
        if not s:
            return True
        if all(p < t for p in s):
            return True
        else:
            continue
    return False


idxs = [(i, x) for i in range(len(data)) for x in range(len(data[0])) ]
vis = [is_visible(idx) for idx in idxs]
print(f"Result1: {sum(vis)}")

# Puzzle 2
from functools import reduce
score = lambda lst: reduce(lambda a, b: a * b, lst)
score_best = 0
edges = ((0, 0), (max([x[0] for x in idxs]), max([x[1] for x in idxs])))
for i, idx in enumerate(idxs):
    if any([a==b for cor in edges for a, b in zip(idx, cor)]):
        continue
    treecount_bool = [[x < data[idx[0]][idx[1]] for x in s] for s in create_tree_neighbours(idx)]
    count = []
    for lst in treecount_bool:
        c = 0
        for b in lst:
            if b:
                c += 1
            else:
                break
        if len(lst) != c:
            c += 1
        count.append(c)
    score_best = max(score_best, score(count))

print(f"Result2: {score_best}")



