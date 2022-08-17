#set union
A = {1, 2, 3, 4, 5, 6, 8, 9, 10, 11}
B = {4, 5, 6, 7, 8, 12, 13}
print(A | B)              # use | operator
print(A.union(B))         # use union function
print(B.union(A))


# set intersection
A = {1, 2, 3, 4, 5, 6, 8, 9, 10, 11}
B = {4, 5, 6, 7, 8, 12, 13}
print(A & B)              # use & operator
print(A.intersection(B))  # use intersection function
print(B.intersection(A))


# set difference
A = {1, 2, 3, 4, 5, 6, 8, 9, 10, 11}
B = {4, 5, 6, 7, 8, 12, 13}
print(A - B)              # use - operator
print(A.difference(B))    # use difference function
print(B - A)

# symmetric difference
A = {1, 2, 3, 4, 5, 6, 8, 9, 10, 11}
B = {4, 5, 6, 7, 8, 12, 13}
print(A ^ B)                          # use ^ operator
print(A.symmetric_difference(B))      # use symmetric_differnce function

# subset
x = {1, 2, 3, 4, 5, 6}
y = {2, 3, 4, 5, 6, 7, 8, 9}
print(x.issubset(y))
z = {3, 4, 5, 10, 11}
print(x.issubset(z))
a = {11, 12, 13}
print(a.isdisjoint(y))

# list-> set-> list
X = [2, 2, 3, 3, 4, 4, 5, 5]
XS =  set(X)
Xl = list(set(X))
print(X)
print(XS)
print(Xl)