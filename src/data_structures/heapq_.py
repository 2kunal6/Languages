# PriorityQueue is synchronized while heapq is not
# runtime
# maxheap: via heapq max_heapify, * -1, creating a new class (see __lt__)
import heapq
from queue import PriorityQueue


c = []
heapq.heappush(c, (2, 'x'))
heapq.heappush(c, (-1, 'x'))
heapq.heappush(c, (5, 'x'))
heapq.heappush(c, (100, 'x'))
heapq.heappush(c, (0, 'x'))
heapq.heappush(c, (6, 'x'))

print(c)

pq = PriorityQueue()
pq.put(2)
pq.put(-1)
pq.put(5)
pq.put(100)
pq.put(0)
pq.put(6)

while(not pq.empty()):
    print(pq.get(), end = ' ')
print()
