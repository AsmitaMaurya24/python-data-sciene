name = 'Asmita Maurya'

#first name
firstname = name[:7]
print(firstname)

#second name
secondname = name[-6:]
print(secondname)

#even_index
even_index = name[::2]
print(even_index)

#odd_index
odd_index = name[1::2]
print(odd_index)

#reversing a string using slicing
reversed_name = name[::-1]
print(reversed_name)

print(name[:]) #won't efffect
print(name[::-1][:7][::-1])


print(name[3:-3])