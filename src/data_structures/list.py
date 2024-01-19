l = []
l.append(2)
l.append(1)
l.append(2)

print(l)

l.insert(1, 100)

print(l)

l.extend(['a', 'bc', -5])

print(l)



# reverse -----------------------------
l.reverse()
print(l)

rl = list(reversed(l))
print(l)
print(rl)


# remove -----------------------------
# removes only the first element in the list with given value
# throws error if value does not exist
l.remove(2)
print(l)
if('not_exist' in l):
    l.remove('not_exist')
print(l)

# pop --------------------------------
# removes last element of the list
# if argument provided then removes that indexed element (FROM THE FRONT)
print('pop')
l.pop()
print(l)
l.pop(3)
print(l)
if(len(l)>=20):
    l.pop(20)
print(l)


l.extend([5, 50, 6, 50, 'z', 50])
print(l)

# slicing -----------------------------
print(l[:2])
print(l[:-2])
print(l[2:])
print(l[::-1]) # reverse


# List Comprehension -------------------
print(str(type(l[0])))
new_l = [x/2 for x in l if type(x) is int]
print(new_l)


# Remove -------------------------------
print(l)
#l.remove(1000)
l.remove(50)
print(l)


# Index ---------------------------------
print(l.index(100))
# print(l.index(100, 0, 2))

# Count ---------------------------------
print(l.count(50))
print(l.count(-1000))

# Sort only works if element types similar
#l.sort()


# Copy
print(l)
l2 = l # changes made to l2 will be reflected in l
l2.pop()
print(l)

l2 = l.copy()
l2.pop()
print(l2)
print(l)

del l[1:3]
print(l)

l.clear()
print(l)


# List Comprehension
cl = [(x, y) for x in (1, 2, 3) for y in (2, 4) if x!=y]
print(cl)

l = [1, -1, 4, 2, -5]
nl = [x for x in l if x<0]
print(nl)

mat = [[1, 2, 3],
       [4, 5, 6]]
print([x for n in mat for x in n])


# List of List
ll = []
ll.append([5, 2])
ll.append([3, 5])
ll.append([1, 1])
ll.append([20, 6])
ll.append([-3, 10])
print(ll[1][1])
ll.sort()
print(ll)
ll.sort(key=lambda x:x[1])
print(ll)
