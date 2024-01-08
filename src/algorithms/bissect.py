from bisect import bisect_left
from bisect import bisect_right


sorted_list = [-1, 10, 10, 100, 199, 200, 2000]

print(bisect_left(sorted_list, -10))
print(bisect_left(sorted_list, -1))
print(bisect_left(sorted_list, 5))
print(bisect_left(sorted_list, 10))
print(bisect_left(sorted_list, 3000))

print('bisect right')
print(bisect_right(sorted_list, -10))
print(bisect_right(sorted_list, -1))
print(bisect_right(sorted_list, 5))
print(bisect_right(sorted_list, 10))
print(bisect_right(sorted_list, 3000))

print('range')

print(bisect_right(sorted_list, 5, 0, 1))
print(bisect_right(sorted_list, 5, 2, 2))
print(bisect_right(sorted_list, 10, 0, 1))
print(bisect_right(sorted_list, 10, 0, 2))
print(bisect_left(sorted_list, 10, 0, 1))
