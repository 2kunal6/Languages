from queue import PriorityQueue


def print_pq(pq):
    for val in pq.queue:
        print((val))

    print((pq.qsize()))

    while not pq.empty():
        print(pq.get())

    print((pq.qsize()))

# second element is not considered
# For these types use tuple or vector
pq = PriorityQueue()
pq.put('j', 1)
pq.put('c', 1)
pq.put('w', 1)
pq.put('b', 1)
pq.put('aj', 1)
pq.put('p', 1)
print_pq(pq)

single_element_pq = PriorityQueue()

single_element_pq.put(10)
single_element_pq.put(100)
print_pq(single_element_pq)
