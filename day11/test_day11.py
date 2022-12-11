
from collections import defaultdict
from typing import Callable

data = open('day11/sample11.txt', 'r').read().split('\n\n')
# data = open('day11/input11.txt', 'r').read().split('\n\n')
dm = [s.split('\n') for s in data]

monk = defaultdict(dict)
insp = defaultdict(int)

def monkey_factory(ms):
    m = int(ms[0].strip(':').split(' ')[1])
    monk[m]['items']: list = [int(x) for x in ms[1].split(': ')[1].split(', ')]
    monk[m]['oper']: Callable = lambda old: eval(ms[2].split('= ')[1])
    monk[m]['test']: int = int(ms[3].split(' ')[-1])
    monk[m]['true']: int = int(ms[4].split(' ')[-1])
    monk[m]['false']: int = int(ms[5].split(' ')[-1])

for m in dm:
     monkey_factory(m)

rounds = 20
for _ in range(rounds):
    for m in monk.keys():
        while items:=monk[m]['items']:
            it = items[0]
            print('')
            print(m, it)
            print(monk[m])
            insp[m] += 1
            monk[m]['items'].pop(0)
            it = monk[m]['oper'](it)
            it //= 3
            test = it % monk[m]['test'] == 0
            if test:
                monk[monk[m]['true']]['items'].append(it)
            else:
                monk[monk[m]['false']]['items'].append(it)
            print(it, test)
            for t in monk.keys():
                print(t, monk[t]['items'], insp[t])

mb = sorted(insp.values())[-2] * sorted(insp.values())[-1]
assert mb == 10605
print(f'Result1: {mb}')