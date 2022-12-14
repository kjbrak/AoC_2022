from collections import defaultdict

data = open('day12/input12.txt', 'r').read().split('\n')
grid = (len(data[0]) ,len(data))
ps_l, pe_l = 'a', 'z'
[ps] = [(x,y) for y,row in enumerate(data) for x,s in enumerate(row) if s=='S']
[pe] = [(x,y) for y,row in enumerate(data) for x,s in enumerate(row) if s=='E']

def ptl(p): # position to letter map
    [l] = [pe_l if p==pe else ps_l if p==ps else data[j][i] for i,j in [p]]
    return l

def neighbours(p) -> list:
    neigh = [(x,y) for y,row in enumerate(data) for x,s in enumerate(row)
            if (x-p[0] in [-1,1] and y==p[1]) | (y-p[1] in [-1,1] and x==p[0])]
    return neigh

def neighbours_criteria(p) -> list:
    n = neighbours(p)
    nc = [px for px in n if (ord(ptl(px))-ord(ptl(p)) < 2)]
    return nc

nodes = [(x, y) for y,row in enumerate(data) for x,s in enumerate(row)]

def search(nodes, p_start, p_end_lst, graph_func):
    graph = defaultdict(list)
    for p in nodes:
        graph[p] = graph_func(p)
    q = list(graph.keys())
    min_cost = {}
    for p in q:
        min_cost[p] = float('inf')
    min_cost[p_start] = 0  # init
    i = 0
    while q:
        print(i)
        q = sorted(q, key=lambda x: min_cost[x])
        p = q.pop(0)
        for px in graph[p]:
            c_min = min_cost[p] + 1
            if c_min < min_cost[px]:
                min_cost[px] = c_min
        if p in p_end_lst:
            print(f"Success!")
            break
        i += 1
    return min_cost


res = search(nodes, ps, [pe], neighbours_criteria)[pe]
print(f"Result1: {res}")

# Puzzleboy 2 Turbo ->
def neighbours_criteria_reverse(p) -> list:
    n = neighbours(p)
    nc = [px for px in n if (ord(ptl(px))-ord(ptl(p)) >= -1)]
    return nc
p_a_lst = [px for px in nodes if ptl(px)=='a'] # All a level points
min_cost2 = search(nodes, pe, p_a_lst, neighbours_criteria_reverse)
res2 = min([v for k,v in min_cost2.items() if ptl(k)=='a'])
print(f"Result2: {res2}")
