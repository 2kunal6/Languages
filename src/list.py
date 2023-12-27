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


l.extend([5, 50, 6, 'z'])
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
