import heapq

c = []
heapq.heappush(c, (2, 'x'))
heapq.heappush(c, (-1, 'x'))
heapq.heappush(c, (5, 'x'))
heapq.heappush(c, (100, 'x'))
heapq.heappush(c, (0, 'x'))
heapq.heappush(c, (6, 'x'))

print(c)
