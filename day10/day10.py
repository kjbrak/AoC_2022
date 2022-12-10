data = open('day10/input10.txt', 'r').read().split('\n')
cycles = [(x*40)+20 for x in range(6)]
c = 0
x = 1
states = []


def state_factory():
    global c, x
    c += 1
    states.extend([(c, x)])


for s in data:
    if s[0] == 'n':
        state_factory()
    else:
        n = int(s.split()[1])
        for _ in range(2):
            state_factory()
        x += n


ss = [c * x for c,x in states if c in cycles]
print(f"Result1: {sum(ss)}")


# Puzzle 2

def is_lit(pix_state):
    return True if pix_state[0] in [pix_state[1] + i for i in range(-1, 2)] else False


grid = (40, 6)
assert len(states)/grid[1] == grid[0] # Check that grid matches cycle count
pix_states = [((a-1)%grid[0], b) for a,b in states]
pix = [is_lit(pix_state) for pix_state in pix_states]
idxs = list(range(0, len(states) + grid[0], grid[0]))
pix_lsts = [pix[a:b] for a,b in zip(idxs, idxs[1:])]

print( '\n'.join([''.join(l)
                   for l in [['#' if test else '.' for test in lst]
                             for lst in pix_lsts ]]
                  ))

