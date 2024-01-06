# recursive and non-recursive bfs and dfs
# directed and non-directed graphs
from collections import deque

g = {}

def insert(v1, v2):
    if(v1 not in g):
        g[v1] = []
    if(v2 not in g):
        g[v2] = []
    g[v1].append(v2)
    g[v2].append(v1)


def bfs():
    print('bfs:')
    vis = {}
    for v in g:
        if(v in vis):
            continue
        q = deque()
        q.append(v)
        while(len(q) > 0):
            val = q.popleft()
            if(val in vis):
                continue
            print(val)
            vis[val] = True
            for item in g[val]:
                q.append(item)

def dfs():
    print('dfs')
    vis = {}
    for v in g:
        if(v in vis):
            continue
        stack = []
        stack.append(v)
        while(len(stack) > 0):
            val = stack.pop()
            if(val in vis):
                continue
            vis[val] = True
            print(val)
            for neigh in g[val]:
                stack.append(neigh)



insert(1, 2)
insert(2, 5)
insert(1, 6)
insert(3, 2)
insert(-1, 3)
insert(1, 7)

bfs()
dfs()
