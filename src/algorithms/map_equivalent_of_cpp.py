l = [2, 6, 10, 5, -1, 4, 3]

n = len(l)

next_upper = [0] * n
next_lower = [0] * n

next_upper[n-1] = l[n-1]
for i in range(n-2, -1, -1):
    if(l[i] > next_upper[i+1]):
        next_upper[i] = l[i]
    else:
        next_upper[i] = next_upper[i+1]

next_lower[n-1] = l[n-1]
for i in range(n-2, -1, -1):
    if(l[i] < next_lower[i+1]):
        next_lower[i] = l[i]
    else:
        next_lower[i] = next_lower[i+1]

print(next_upper)
print(next_lower)
