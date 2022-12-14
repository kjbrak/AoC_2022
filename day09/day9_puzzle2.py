#TODO: move func could be updated to reflect "new" rope rules and used on multiple knots.
from collections import defaultdict

data = open('day09/in9', 'r').read().split('\n')


def move(pos, dir):
    x,y = pos
    (i,) = [-1 if dir in 'LD' else 1]
    if s[0] in 'LR':
        x += i
    else:
        y += i
    pos = (x, y)
    return pos


pos = {k:(0,0) for k in range(10)}
pos_new = pos.copy()
d = defaultdict(int)
d[(0,0)] += 1
for s in data:
    dir = s[0]
    num = int(s[2:])
    for _ in range(num):
        pos[0] = move(pos[0], dir)
        for k in list(pos.keys())[1:]:
            dx, dy = [h - t for h,t in zip(pos[k-1], pos[k])]
            if any([abs(diff) > 1 for diff in [dx, dy]]):
                x, y = pos[k]
                if abs(dx) > 0:
                    (xmove,) = [1 if dx > 0 else -1]
                    x += xmove
                if abs(dy) > 0:
                    (ymove,) = [1 if dy > 0 else -1]
                    y += ymove
                pos[k] = (x, y)
        d[pos[len(pos)-1]] += 1

print(f"Result2: {len(d)}")