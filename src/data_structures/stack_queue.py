from collections import deque

queue = deque([1, 2, 3])
queue.append(4)
print(queue.popleft())
while(len(queue)>0):
    print(queue.popleft())

print('stack')
stk = []
stk.append(1)
stk.append(2)
stk.append(3)
val = stk.pop()
print(val)
stk.append(4)
while(len(stk) > 0):
    print(stk.pop())


