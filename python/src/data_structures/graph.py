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
            print(val, end = ' ')
            vis[val] = True
            for item in g[val]:
                q.append(item)
    print()

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
            print(val, end = ' ')
            for neigh in g[val]:
                stack.append(neigh)
    print()

def dfs_r(v, vis):
    if(v in vis):
        return
    print(v, end = ' ')
    vis[v] = True
    for val in g[v]:
        dfs_r(val, vis)

def dfs_recursive():
    print('dfs recursive')
    vis = {}
    for v in g:
        if(v not in vis):
            dfs_r(v, vis)


insert(1, 2)
insert(2, 5)
insert(1, 6)
insert(3, 2)
insert(-1, 3)
insert(1, 7)

bfs()
dfs_recursive()
dfs()


# directed graph ----------------------------------
print('directed')
dg = {}

def insert(v1, v2):
    if(v1 not in dg):
        dg[v1] = []
    if(v2 not in dg):
        dg[v2] = []
    dg[v1].append(v2)

insert(1, 2)
insert(2, 5)
insert(1, 6)
insert(3, 2)
insert(-1, 3)
insert(7, 1)

def bfs_d():
    vis = {}
    q = deque()
    for v in dg:
        if(v in vis):
            continue
        q.append(v)
        while(len(q) > 0):
            val = q.popleft()
            if(val in vis):
                continue
            print(val, end = ' ')
            vis[val] = True
            for nb in dg[val]:
                q.append(nb)
    print()


def dfs_d():
    vis = {}
    stk = []
    for v in dg:
        if(v in vis):
            continue
        stk.append(v)
        while(len(stk) > 0):
            val = stk.pop()
            if(val in vis):
                continue
            vis[val] = True
            print(val, end = ' ')
            for nb in dg[val]:
                stk.append(nb)
    print()


bfs_d()
dfs_d()
