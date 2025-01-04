# We can use any immutable data types as key to Python Dictionaries
# Ex. Tuple, Boolean, String etc.
# but only if the Tuple does not contain any mutable type
# Multimap equivalent: use dict and a list as the value

dict = {}
dict['c'] = 1
dict['a'] = 5

for key, val in dict.items():
    print(key, val)

print(dict['a'])
print('z' in dict.keys())
print('z' in dict)

print(dict)
del dict['a']
print(dict)
print('list dict: ', list(dict))


int_dict = {}
int_dict[1] = 1
int_dict[2] = 1
print(int_dict)

# Not Possible since list is mutable
list_dict = {}
#list_dict[[1, 2, 3]] = 1
#list_dict[[1, 2, 3, 4]] = 1
