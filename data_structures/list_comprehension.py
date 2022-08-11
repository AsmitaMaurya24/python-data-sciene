x = [2, 3, 4, 5, 6, 7, 8]
x2 = [i ** 2 for i in x]
print(x)
print(x2)
y = [2, 3, 4, 5, 6, 7, 7, 2]

z = [i + j for i,j in zip(x,y)]
print(z)

names = ['Asmita Maurya', 'Ayushi Chandra', 'Aparna Sharma']
initials = []
for name in names:
    parts = name.split()
    initials.append(parts[0][0] + parts[-1][0])
print(initials)

names = ['Asmita Maurya', 'Ayushi Chandra', 'Aparna Sharma']
initials = [name.split()[0][0] + name.split()[-1][0] for name in names]
print(initials)

