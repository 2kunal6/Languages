# PriorityQueue is synchronized while heapq is not
# runtime: Implemented using binary heap. O(log n) for both push and pop
import heapq
from queue import PriorityQueue


c = []
heapq.heappush(c, (2, 'x'))
heapq.heappush(c, (-1, 'x'))
heapq.heappush(c, (5, 'x'))
heapq.heappush(c, (100, 'x'))
heapq.heappush(c, (0, 'x'))
heapq.heappush(c, (6, 'x'))

while(len(c) > 0):
    print(heapq.heappop(c), end = ' ')
print()

c = [2, -1, 5, 100, 0, 6]
heapq._heapify_max(c)
while(len(c) > 0):
    print(heapq._heappop_max(c), end = ' ')
print()

c = [2, -1, 5, 100, 0, 6]
c_max_pq = []
for val in c:
    heapq.heappush(c_max_pq, -1*val)
while(len(c_max_pq) > 0):
    print(-1*heapq.heappop(c_max_pq), end = ' ')
print()


pq = PriorityQueue()
pq.put(2)
pq.put(-1)
pq.put(5)

while(not pq.empty()):
    print(pq.get(), end = ' ')
print()


class MaxHeapElement:
    def __init__(self, val):
        self.val = val
    def __lt__(self, other):
        return self.val > other.val
    def __str__(self):
        return str(self.val)

max_pq = PriorityQueue()
max_pq.put(MaxHeapElement(2))
max_pq.put(MaxHeapElement(-1))
max_pq.put(MaxHeapElement(5))

while(not max_pq.empty()):
    print(max_pq.get(), end = ' ')
print()

max_pq_minus_1 = PriorityQueue()
mpq_list = [9, 4, -1, 100, 3]
for val in mpq_list:
    max_pq_minus_1.put((-1*val))
while(not max_pq_minus_1.empty()):
    print(-1*max_pq_minus_1.get(), end=' ')
print()
