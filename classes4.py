class Student:
	
	passPercentage = 40
	
	def studentDetails(self):
		self.name = 'Parikh'
		print("Name is ", self.name)

		self.percentage = 80
		print('Percentage is ', self.percentage)

	def isPassed(self):
		if self.percentage >= Student.passPercentage:
			print("Person has passed")

		else:
			print("Person has failed")

	@staticmethod
	def WelcomeToSchool():
		print("Hey, Welcome to School!")

	@staticmethod
	def WelcomeToSchool2(self):
		print("Welcome to School2, with a self in staticmethod, you will get error :p")


s1 = Student()


Student.studentDetails(s1)
s1.studentDetails() # == Student.studentDetails(s1)
s1.isPassed()
s1.WelcomeToSchool()
s1.WelcomeToSchool2()