"""
Note: this code will fail on assertion. It is for a more fluid rope with different rules than intended by the puzzle maker
"""

from collections import defaultdict

data = open('day9/sample2_in9', 'r').read().split('\n')
# data = open('day9/sample_in9', 'r').read().split('\n')


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
    for i in range(num):
        pos_new[0] = move(pos[0], dir)
        for k in list(pos.keys())[1:]:
            if any([abs(h - t) > 1 for h,t in zip(pos_new[k-1], pos[k])]):
                pos_new[k] = pos[k-1]
        pos = pos_new.copy()
        d[pos[len(pos)-1]] += 1

# Assertion error -> Note: rope does not follow the best rules, that is working in puzzle 1 !
res2 = len(d)
print(f"Result2: {res2}")
# assert res2 == 36