from datetime import date

class Student:
	passPercentage = 40

	def __init__(self, name, age=20, percentage=25):
		self.name = name
		self.age = age
		self.percentage = percentage

	@classmethod
	def fromBirthYear(cls, name, year, percentage):
		return cls(name, date.today().year - year, percentage)

	def printStudentDetails(self):
		print("Name is ", self.name)
		print('Age is', self.age)
		print('Percentage is', self.percentage)

s1 = Student('parikh')
s2 = Student.fromBirthYear('Ankush', 1996, 30)
s1.printStudentDetails()
s2.printStudentDetails()
