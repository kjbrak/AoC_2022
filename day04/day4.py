data = open('day04/in4', 'r').read().split('\n')

# Puzzle1
l = [tuple(s.replace('-',',').split(',')) for s in data]
lst = [tuple(int(s) for s in li) for li in l]
crit = [i for i,tup in enumerate(lst) if ((tup[0]>=tup[2] and tup[1]<=tup[3]) | (tup[2]>=tup[0] and tup[3]<=tup[1])) ]
print(f'Result1: {len(crit)}')

# Puzzle2
c = [i for i,tup in enumerate(lst) if ((tup[1]>=tup[2] and tup[0]<=tup[3]) | (tup[3]>=tup[0] and tup[2]<=tup[1])) ]
print(f'Result2: {len(c)}')