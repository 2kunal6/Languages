from queue import PriorityQueue

pq = PriorityQueue()

pq.put('j', 1)
pq.put('c', 1)
pq.put('w', 1)
pq.put('b', 1)
pq.put('aj', 1)
pq.put('p', 1)

print((pq.qsize()))

while not pq.empty():
    print(pq.get())

print((pq.qsize()))
