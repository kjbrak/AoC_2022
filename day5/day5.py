import re
import copy

data_stacks, data_proc = (s.split('\n') for s in open('day5/in5', 'r').read().split('\n\n'))
l_tot = 9 * 3 + 9
sl = [s+' '*(l_tot-len(s)) for s in data_stacks[:-1]]
s_lst = [[re.sub('[\[\]]','', s[i:i+4]).strip() for i in range(0, len(s), 4)] for s in sl]

# Just in case..
if not all([l==len(s_lst[0]) for l in map(len, s_lst)]):
    raise ValueError('The list lengths are not the same!')

stacks = [list(reversed(x)) for x in list(map(list, zip(*s_lst))) ]
stacks = [[x for x in lst if len(x)>0] for lst in stacks]
moves = [tuple(map(int, tup)) for tup in [ tuple(re.findall(r'\d+', s)) for s in data_proc ]]
moves = [tup for tup  in moves if len(tup)>0]
stacks_original = copy.deepcopy(stacks)


def move(tup, stacks, crane_model='CrateMover 9000'):
    m = []
    for n in range(tup[0]):
        m.append(stacks[tup[1]-1].pop())
    if crane_model.lower() == 'cratemover 9001':
        m = list(reversed(m))
    stacks[tup[2]-1].extend(m)
    return stacks


for tup in moves:
    stacks = move(tup, stacks)

res = ''.join([lst[-1] for lst in stacks])
print(f"Result1:  {res}")

# Puzzle 2
stacks = copy.deepcopy(stacks_original)
for tup in moves:
    stacks = move(tup, stacks, crane_model='CrateMover 9001')

res = ''.join([lst[-1] for lst in stacks])
print(f"Result2:  {res}")

