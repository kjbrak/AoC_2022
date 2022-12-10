from copy import deepcopy

data = open('day07/in7', 'r').read().split('\n')
filesize_max = 100000
tree = {}
cursor = '/'
for s in data:
    if s.startswith('$'):
        if 'cd' in s:
            dir = s[s.index('cd') + 3:]
            if dir == '..':
                if len(cursor.split('/')) > 2:
                    cursor = '/'.join(cursor.split('/')[:-1])
                else:
                    cursor = '/'
            elif dir[0] != '/' and cursor != '/':
                cursor = f'{cursor}/{dir}'
            elif dir[0] != '/':
                cursor = f'{cursor}{dir}'
            else:
                cursor = dir
            if cursor not in tree:
                tree[cursor] = []
        elif 'ls' in s:
            continue
    else:
        if s.startswith('dir'):
            tree[cursor].append(('dir',s[4:]))
        else:
            tree[cursor].append(('file',s.split()[1], int(s.split()[0])))

import re
siz = {k:0 for k in tree.keys()}
prev = 1
while prev != siz:
    prev = deepcopy(siz)
    for k,v in tree.items():
        siz[k] = sum([tup[2] for tup in v if len(tup) == 3])
        if k == '/':
            subdirs = [s for s in tree.keys() if all([s.startswith(k),
                                                      s.split('/')[-2] == k.split('/')[-1],
                                                      ])]

        else:
            subdirs = [s for s in tree.keys() if all([s.startswith(k),
                                                      s.split('/')[-2] == k.split('/')[-1],
                                                      len(s.split('/')) == len(k.split('/')) + 1,
                                                      ])]
        for sd in subdirs:
            siz[k] += siz[sd]


lst = [v for v in siz.values() if v <= filesize_max]
print(f'Result1: {sum(lst)}')

# Puzzle 2 ->
tot_space = 70000000
space_need = 30000000
unused_space = tot_space - siz['/']
claim = space_need - unused_space
d = min([v for k,v in siz.items() if v > claim])
print(f'Result2: {d}') # 1077191



