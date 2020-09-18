class Student:
	pass

s1 = Student()
s2 = Student()
s3 = Student()

print(s1, s2, s3)

s1.name = "Ankur"

print(s1.__dict__, s2.__dict__)

s2.rollNum = 12

s3.name = "Rohan"
s3.rollNum = 13

print(s1.__dict__, s2.__dict__, s3.__dict__)

print(hasattr(s1, "name"))
print(hasattr(s2, "name"))

print(getattr(s1, 'name'))
print(getattr(s2, 'name', 'exception raised'))

print(delattr(s1, "name"))
print(s1.__dict__)


print(delattr(s1, "name"))