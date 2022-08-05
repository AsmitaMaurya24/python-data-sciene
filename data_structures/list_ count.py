# count function
x = [1,1,1,1,1,3,3,3,3,4,4,4,4,4,6]

print('totoal no. of 1 =',x.count(1))
print('totoal no. of 3 =',x.count(3))
print('totoal no. of 4 =',x.count(4))

# index function
movies = ['Batman', 'DDLJ', 'Dragon', 'Inception', 'Avengers', 'KGF', 'RRR', 'Majili', 'Anaconda']

print(movies.index('Majili'))
print(movies.index('Dragon'))


# copy function
block_busters = movies.copy()
print('duplicated list =',block_busters)

# clear function
block_busters.clear()
print('After clearing block busters =', block_busters)

print('After poping = ', movies.pop())
print('After poping index 4 = ', movies.pop(4)) 
print('After poping index 5 = ', movies.pop(5))
print('After poping unavailable index 11 = ', movies.pop(11))






