my_set = {1, 5, 7, 5}
print(my_set)

s1 = set()
s1.add(5)
s1.add(2)
s1.add(5)
print(s1)

print(10 in s1)

print(my_set - s1)
print(my_set | s1)
print(my_set & s1)
print(my_set ^ s1) # In my_set or s1, but not both
