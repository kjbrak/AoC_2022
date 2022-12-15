data = [[tuple(int(i)
               for i in t.split(','))
         for t in s.split(' -> ')]
        for s in open('day14/sample.txt', 'r').read().split('\n')]
        # for s in open('day14/input.txt', 'r').read().split('\n')]

src = (500, 0)
# grid_max = (max([tup[0] for lst in data for tup in lst]), max([tup[1] for lst in data for tup in lst]))
# grid_min = (min([tup[0] for lst in data for tup in lst]), min([tup[1] for lst in data for tup in lst]))
# grid = [(x, y) for y in [yy for yy in range(grid_min[1]+1)] for x in range(grid_min[0], grid_max[0]+1)]



# fill = [False] * len(grid)
def fill_with_rocks(data):
    rocks_fill = set()
    for i, lst in enumerate(data):
        print(lst)
        # i, lst = 0, data[0]
        for j, p1 in enumerate(lst[:-1]):
            # j, p1 = 0, lst[0]
            p2 = lst[j+1]
            print(p1, '--->', p2)
            # points = []
            if p1[0] == p2[0]:
                y_lst  = sorted((p1[1], p2[1]))
                y_range = range(y_lst[0], y_lst[1] + 1)
                points = [(p1[0], y) for y in y_range]
            elif p1[1] == p2[1]:
                x_lst  = sorted((p1[0], p2[0]))
                x_range = range(x_lst[0], x_lst[1] + 1)
                points = [(x, p1[1]) for x in x_range]
            else:
                raise ValueError('Rock scan not strictly vertical/horizontal!')
            rocks_fill |= set(points)
    return rocks_fill

rocks_fill = fill_with_rocks(data)
sorted(rocks_fill)
fill = rocks_fill.copy()
y_abyss = max([p[1] for p in rocks_fill])
busy = True
i = 1
while busy:
    print('\n### New grain ###')
    falling = True
    grain = src # init
    while falling:
        print('pos:', grain)
        print(i)
        if grain[1] >= y_abyss:
            busy = False
            print(f"Abyss for grain no.: {i} !")
            print(f"Last grain no.: {i-1} !")
            break
        if (p2:=(grain[0], grain[1] + 1)) not in fill:
            grain = p2
            continue
        elif (p2:=(grain[0] - 1, grain[1] + 1)) not in fill:
            grain = p2
            continue
        elif (p2:=(grain[0] + 1, grain[1] + 1)) not in fill:
            grain = p2
            continue
        else:
            print(f'Grain settling: {grain}')
            fill.add(grain)
            falling = False
    i += 1

res = len(fill - rocks_fill)  # tot grains
print(f'Results1: {res}')
assert res == 24

# Puzzle 2
data2 = data.copy()
floor_data = [(int(-1e5), max([p[1] for p in rocks_fill]) + 2), (int(1e5), max([p[1] for p in rocks_fill]) + 2)]
data2.append(floor_data)
rocks_fill = fill_with_rocks(data2)
fill = rocks_fill.copy()
busy = True
i = 1
while busy:
    print('\n### New grain ###')
    falling = True
    grain = src # init
    while falling:
        print('pos:', grain)
        print(i)
        if (p2:=(grain[0], grain[1] + 1)) not in fill:
            grain = p2
            continue
        elif (p2:=(grain[0] - 1, grain[1] + 1)) not in fill:
            grain = p2
            continue
        elif (p2:=(grain[0] + 1, grain[1] + 1)) not in fill:
            grain = p2
            continue
        else:
            print(f'Grain settling: {grain}')
            fill.add(grain)
            falling = False
            if grain == src:
                busy = False
                print(f"Reached source point for grain no.: {i} !")
                # print(f"Last grain no.: {i-1} !")
                break
    i += 1

res2 = len(fill - rocks_fill)  # tot grains (but not here since floor..)
res2 = i-1  # tot grains (but not here since floor..)
print(f'Results2: {res2}')
assert res2 == 93

