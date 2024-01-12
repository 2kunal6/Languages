a_str = 'A basic String'

# find ------------------------------------------
print('basic' in a_str)
print('bAsic' in a_str)
print('bAsic'.lower() in a_str.lower())
print(a_str.find('basic'))
new_str = 'abcjhabjd'
print(new_str.find('ab'))
print(new_str.find('ab', 1))

# substring -------------------------------------

# prints excluding the 6th
print(a_str[2:6])

# prints till end
print(a_str[2:100])
print(a_str[2:])

print(a_str[-6:-4])


# string to int and int to string
print(str(-100))
#print(int('-102.5')) invalid
print(int('-102'))
print(float('-102.5'))
