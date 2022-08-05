# append function
fruits = []
fruits.append('Mango')
fruits.append('Apple')
fruits.append('Banana')
fruits.append('kiwi')

print(fruits)

# insert function
fruits.insert(2,'strawberry')
print(fruits)

dry_fruits = ['Almonds', 'Cashew', 'Walnut', 'Dates', 'Raisins']
fruits.extend(dry_fruits)
print(fruits)

# sort function
fruits = ['Cherry', 'Guava', 'Apple', 'Banana']
fruits.sort()
print(fruits)

# remove function
fruits.remove('Cherry')
print(fruits)

# reverse fuction
fruits = ['Cherry', 'Guava', 'Apple', 'Banana']
fruits.sort(reverse = True)
print(fruits)