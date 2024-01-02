# Tuples are immutable unlike lists
# Meaning, we can't append/remove from tuples

t = (1, 2, 3)
print(t)

t2 = 4, 5, 6
print(t2)

t3 = 'a', 7, 8
print(t3)
# t3[0] = 6 immutable, so this doesn't work

print(t3[1])

single_element_tuple_wrong = (1)
print(single_element_tuple_wrong)
print(type(single_element_tuple_wrong))

single_element_tuple = (1,)
print(single_element_tuple)
print(type(single_element_tuple))

