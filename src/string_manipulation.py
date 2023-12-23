str = 'A basic String'

# find ------------------------------------------
print('basic' in str)
print('bAsic' in str)
print('bAsic'.lower() in str.lower())
print(str.find('basic'))

# substring -------------------------------------

# prints excluding the 6th
print(str[2:6])

# prints till end
print(str[2:100])
print(str[2:])

print(str[-6:-4])
