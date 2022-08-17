# get vs [] for retrieving elements 
my_dict = {'name': 'Jack', 'age': 26}
print(my_dict['name'])     
print(my_dict.get('age'))

#print(my_dict['address'])  # trying to access keys which doesn't exist throws error
print(my_dict.get('address')) # doesn't throw error

# modifying elements from dictionary

# update a value
my_dict['age'] = 27
print(my_dict)
my_dict['address'] = 'Downtown'
print(my_dict)

# removing elements from dictionary

# create a dictionary
squares = { 1:1, 2:4, 3:9, 4:16, 5:25, 6:36}
print(squares.pop(4))
print(squares.pop(5))
print(squares.popitem())     #remove an arbitary item 
squares.clear()              # remove all items
del squares                  # delete dictionary itself

# iterating through a dictionary

# create a dictionary
squares = { 1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49}
for i in squares: # only keys
    print(i)
for i in squares:
    print(squares[i])
for k,v in squares.items():
     print(k,v)
