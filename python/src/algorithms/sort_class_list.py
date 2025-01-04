class Node:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __lt__(self, other):
        return self.b < other.b

    def __str__(self):
        return str(self.a) + ' ' + str(self.b)

l = [Node(10, 7), Node(1, 5), Node(50, 60)]
l.sort()
for val in l:
    print(val)
