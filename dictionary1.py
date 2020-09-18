a = {'the': 5, 'a':10, 100:15}

print(a)

b = a.copy()
print(b)

print(type(b))

c = dict([('the',5),('a',10),(2,3)])
print(c)

d1 = dict.fromkeys(['the', 'a', 100])
print(d1)

d2 = dict.fromkeys(['the', 'a', 100], 'default value')
print(d2)
