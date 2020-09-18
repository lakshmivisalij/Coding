from abc import ABC, abstractmethod
class Automobile(ABC):
	def __init__(self):
		print("Automobile created")
		
	@abstractmethod
	def start(self):
		print("start method of Automobile class called.")

	@abstractmethod
	def stop(self):
		print("stop method of Automobile class called.")

	@abstractmethod
	def drive(self):
		pass
	

class Car(Automobile):
	"""docstring for Car"""
	def __init__(self, name):
		self.name = name
		print("Car created")

	def start(self):
		super().start()
		


	def stop(self):
		print("stop method of Car class called")

	def drive(self):
		pass


		
c = Car('TATA')
c.start()
c.stop()

# a = Automobile() -> Abstract class can be created when there are no abstract methods

# 1. Objects of abstract classes cannot be created
# 2. Must implement all the abstract methods in child class