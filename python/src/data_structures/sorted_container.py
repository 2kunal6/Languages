from sortedcontainers import SortedList

import bisect


input_arr = [6, 8, 0, 1, 3]
n = len(input_arr)
sc = SortedList()

ans = []

for i in range(n-1, -1, -1):
    if(len(sc) == 0):
        ans.append(-1)
    else:
        val = bisect.bisect_right(sc, input_arr[i])
        if(val >= len(sc)):
            ans.append(-1)
        else:
            ans.append(sc[val])
    sc.add(input_arr[i])

ans.reverse()
print(ans)