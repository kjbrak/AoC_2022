
# Input
opp = {'A':'rock', 'B': 'paper', 'C': 'scissors'}
resp= {'X':'rock', 'Y': 'paper', 'Z': 'scissors'}
p = {'rock': 1, 'paper': 2, 'scissors': 3 }
w = {'win': 6, 'draw': 3, 'lose': 0}

fn = 'day02/day2_input.txt'
with open(fn, 'r') as f:
    lines = f.read()
    lst = lines.split('\n')

win_map = {'scissors':'rock', 'rock':'paper', 'paper':'scissors' } # {x :beaten-by: y}

# Output
def event_outcome(a, b):
    if a == b:
        r = 'draw'
    elif a == win_map[b]:
        r = 'lose'
    elif win_map[a] == b:
        r = 'win'
    else:
        raise ValueError('Not a recognised move!')
    return r


def result_tuple_from_string_pair(stringpair):
    s = stringpair.split(' ')
    a = opp[s[0]]
    b = resp[s[1]]
    r = event_outcome(a, b)
    return (r, b)


def calc_points_from_tuple_result_variant(tup):
    points = w[tup[0]] + p[tup[1]]
    return points


res = []
for x in lst:
    res.append(result_tuple_from_string_pair(x))
points = sum([calc_points_from_tuple_result_variant(tup) for tup in res])
print(f'Result1: {points}')


# Task 2
resp2 = {'X':'lose', 'Y': 'draw', 'Z': 'win'}
def result_tuple_from_string_pair_pouzzle2(stringpair):
    s = stringpair.split(' ')
    a = opp[s[0]]
    r = resp2[s[1]]
    lose_map =  {v:k for k,v in win_map.items()}
    [b] = [lose_map[a] if r=='lose' else win_map[a] if r=='win' else a for r in [r]]
    return (r, b)


res2 = []
for x in lst:
    res2.append(result_tuple_from_string_pair_pouzzle2(x))
points2 = sum([calc_points_from_tuple_result_variant(tup) for tup in res2])
print(f'Result2: {points2}')

    

