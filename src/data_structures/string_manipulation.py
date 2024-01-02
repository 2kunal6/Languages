str = 'A basic String'

# find ------------------------------------------
print('basic' in str)
print('bAsic' in str)
print('bAsic'.lower() in str.lower())
print(str.find('basic'))
new_str = 'abcjhabjd'
print(new_str.find('ab'))
print(new_str.find('ab', 1))

# substring -------------------------------------

# prints excluding the 6th
print(str[2:6])

# prints till end
print(str[2:100])
print(str[2:])

print(str[-6:-4])
