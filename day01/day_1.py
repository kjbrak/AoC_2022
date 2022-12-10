# Question 1
fn = 'day01/day1_input.txt'
with open(fn, 'r') as f:
    #line  = map(int, f.readline().split())
    # lines  = f.readlines()
    lines = f.read()
    lst = lines.split('\n')
lst.insert(0, '')
lst.insert(-1, '')
idxs = [i for i, x in enumerate(lst) if x == ""]
tups = list(zip(idxs, idxs[1:]))
groups = [( lst[tup[0]:tup[1]] ) for tup in tups]
g_ints = [[int(x) for x in lzt if len(x)>0] for lzt in groups]
sums = [sum(l) for l in g_ints]
maximum = max(sums)
print(maximum)

# Question 2 (top 3 elves)
sums2 = sums.copy()
top_3 = []
for i in range(0,3):
    top_3.append(max(sums2))
    sums2.pop( sums2.index((max(sums2))) )
sum2 = sum(top_3)
print(sum2)
