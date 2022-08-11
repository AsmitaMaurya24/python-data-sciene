x = [2, 3, 4, 5, 6]
x2= [] #empty
for i in x:
    s = i ** 2
    x2.append(s)

print(x)
print(x2)


x = [2, 3, 4, 5, 6]
y = [3, 4, 5, 6, 7]
z = [] #empty
for i, j in zip(x,y): # zip -> special loop function
    z.append(i+j)
    
print(z)
