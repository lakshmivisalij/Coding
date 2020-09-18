d = {1:2, 3:4, 'list':[3,4], 'dict':{1:'s'}}
print(d)

for i in d:
	print(i)

for i in d:
	print(i, d[i])

print(d['list'])

print(d.get('list'))

print(d.get('li'))
print(d.get('li', 0))

print(d.keys())
print(d.values())
print(d.items())

print('list' in d)
print('li' in d)

a = {1:2, 3:4, 'list':[3,4], 'dict':{1:'s'}}
a['tuple'] = (1,2,3)

b = {5:7, 3:5, 't': (1,2,3)}
a.update(b)

print(a)

print(a.pop(3))

del a[1]

print(a)

a.clear()
print(a)

del a
print(a)