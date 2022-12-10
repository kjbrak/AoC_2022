from collections import defaultdict

data = open('day9/in9', 'r').read().split('\n')


def move(pos, dir):
    x,y = pos
    (i,) = [-1 if dir in 'LD' else 1]
    if s[0] in 'LR':
        x += i
    else:
        y += i
    pos = (x, y)
    return pos


hpos = tpos = (0,0)
d = defaultdict(int)
d[(0,0)] += 1
for s in data:
    dir = s[0]
    num = int(s[2:])
    for _ in range(num):
        hpos_new = move(hpos, dir)
        if any([abs(h - t) > 1 for h,t in zip(hpos_new,tpos)]):
            tpos = hpos
        hpos = hpos_new
        d[tpos] += 1

print(f"Result1: {len(d)}")

