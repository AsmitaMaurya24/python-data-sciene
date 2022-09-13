# tuple with mixed data types
my_tuple = (1, 'Hello', 3.4)
print(my_tuple)


my_tuple = ('mouse', [4, 5,6], (1, 2, 3))
print(my_tuple)


my_tuple = 3, 4, 5.6, 'Apple'
print(my_tuple)


# accessing tuple elements using indexing
my_tuple = ('p, t, y, u, i, o, q, w')
print(my_tuple[0])      # p
print(my_tuple[6])      # y


# nested tuple
n_tuple = ('mouse', [8, 4, 6], (1, 2, 3))
# nested index
print(n_tuple[0][3])     # 's'
print(n_tuple[1][1])     #  4
print(n_tuple[2][0])     #  1


# Accessing tuple elements using slicing
my_tuple = ('e','x','c','a','l','i','b','u','r')


#elements 2nd nd 4th
print(my_tuple[1:4])

#elements beginning to 2nd 
print(my_tuple[:-7])

#elements 8th to end
print(my_tuple[7:])

#elements beginning to the end
print(my_tuple[:])


# Concatenation
print((1, 2, 3) + (4, 5, 6))
print(('Repeat,') * 3)

my_tuple = ('a','p','p','l','e')
print(my_tuple.count('p'))  # output 2
print(my_tuple.index('l'))  # output 3