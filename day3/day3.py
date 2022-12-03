lst = open('day3/parse input_day3 --oneline', 'r').read().split('\n')
l2pri = lambda s: ord(s) - (96 if s.islower() else (64 - 26) if s.isupper() else ValueError('shit!'))
print(f'Result1: {sum([l2pri(s) for s in [str(*s) for s in [set(s[:int(len(s)/2)]).intersection(set(s[int(len(s)/2):])) for s in lst] if len(s)>0]])}')
print(f'Result2: {sum([l2pri(*s) for s in [set.intersection(*[set(x) for x in l]) for l in [lst[k:k+3] for k in range(0, len(lst), 3)]]])}')