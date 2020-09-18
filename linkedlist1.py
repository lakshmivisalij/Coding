class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

newNode1 = Node(15)
newNode2 = Node(13)

newNode1.next = newNode2

print(newNode1.data)
print(newNode2.data)
print(newNode1.next.data)