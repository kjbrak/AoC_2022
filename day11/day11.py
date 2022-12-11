from collections import defaultdict
from typing import Callable, DefaultDict


def monkey_factory(ms):
    m = int(ms[0].strip(':').split(' ')[1])
    monk[m]['items']: list = [int(x) for x in ms[1].split(': ')[1].split(', ')]
    monk[m]['oper']: Callable = lambda old: eval(ms[2].split('= ')[1]) # note: unsafe, use with trusted data only
    monk[m]['test']: int = int(ms[3].split(' ')[-1])
    monk[m]['true']: int = int(ms[4].split(' ')[-1])
    monk[m]['false']: int = int(ms[5].split(' ')[-1])


def simulate(rounds:int, stress_func: Callable, monk_in: DefaultDict):# init
    monk = {k:v for k,v in monk_in.items()}
    insp = defaultdict(int)
    for _ in range(rounds):
        for m in monk.keys():
            while items:=monk[m]['items']:
                it = items[0]
                insp[m] += 1
                monk[m]['items'].pop(0)
                it = monk[m]['oper'](it)
                it = stress_func(it)
                test = it % monk[m]['test'] == 0
                if test:
                    monk[monk[m]['true']]['items'].append(it)
                else:
                    monk[monk[m]['false']]['items'].append(it)

    return sorted(insp.values())[-2] * sorted(insp.values())[-1]


if __name__ == '__main__':
    monkey_lst = [s.split('\n') for s in open('day11/input11.txt', 'r').read().split('\n\n')]
    monk = defaultdict(dict)
    for m in monkey_lst:
         monkey_factory(m)

    # Puzzle 1 -->
    def stress_func1(it):
        return it//3

    print(f'Result1: {simulate(20, stress_func1, monk)}')

    # Puzzle 2 -->
    import math
    div = list(set([monk[x]['test'] for x in monk.keys()]))
    lcm = math.lcm(*div)

    def stress_func2(it):
         return lcm + it % lcm

    print(f'Result2: {simulate(10000, stress_func2, monk)}')