a = [1,2,3,4,5,3,2,2,4,5,6,6,4,3,3,3,2,1,1,]

clean_a = list(filter(lambda i: i!= 1, a))
print(clean_a)

files = ['a.png', 'b.png', 'c.jpg', 'd.jpg']
jpeg = list(filter(lambda name: name.endswith('.jpg'), files))
png = list(filter(lambda name: name.endswith('.png'), files))
print(jpeg)
print(png)