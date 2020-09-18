class Student:
	def __init__(self, name, rollNumber):
		self.name = name
		self.rollNum = rollNumber

s1 = Student('Ankush', 12)
s2 = Student('Rohan', 13)
s3 = Student('Priya', 14)

print(s1.__dict__ ,s2.__dict__ ,s3.__dict__)