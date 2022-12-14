from itertools import zip_longest
from ast import literal_eval
from functools import cmp_to_key


data = [s.split('\n') for s in open('day13/input13.txt', 'r').read().split('\n\n')]


def compare_ints(a, b):
    if a < b:
        return 1
    elif b < a:
        return -1
    return 0


def compare(a, b, verbose=False):
    test = 0
    if verbose:
        print(a,'#',b)
    if isinstance(a, int) and isinstance(b, int):
        test = compare_ints(a, b)
    elif isinstance(a, list) and isinstance(b, list):
        for le, r in zip_longest(a, b):
            if verbose:
                print(le,'#',r)
            if le == None:
                return 1
            elif  r == None:
                return -1
            temp = compare(le, r)
            if temp == 0:
                continue
            else:
                test = temp
                break
    elif isinstance(a, int) and isinstance(b, list):
        test = compare([a], b)
    elif isinstance(a, list) and isinstance(b, int):
        test = compare(a, [b])
    else:
        raise ValueError('! no Match!')
    return test


res = []
i = 0
for lst in data:
    l, r = [literal_eval(s) for s in lst]
    print('########')
    print(i)
    print(f'#{l}\n#{r}')
    res.append(compare(l, r, verbose=True))
    print(res[-1])
    i += 1


idx = [i+1 for i,x in enumerate(res) if x==1]
res = sum(idx)
print(f'Result1: {res}')

# Puzzle 2
div_packets = ['[[2]]','[[6]]']
data2 = data.copy()
order = [el for lst in data2 for el in lst]  # unpacking all pairs
order.extend(div_packets)
order = [literal_eval(s) for s in order]
new_order = sorted(order, key=cmp_to_key(compare), reverse=True)
idxs = [i+1 for i,x in enumerate(new_order) if x in [literal_eval(s) for s in div_packets]]
res2 = idxs[0]* idxs[1]
print(f'Result2: {res2}')