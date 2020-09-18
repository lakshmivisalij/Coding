class Vehicle:
	def __init__(self, color, maxSpeed):
		self.color = color
		self.__maxSpeed = maxSpeed

	def getMaxSpeed(self):
		return self.__maxSpeed

	def setMaxSpeed(self, maxSpeed):
		self.__maxSpeed = maxSpeed

class Car(Vehicle):

	def __init__(self, color, maxSpeed, numGears, isConvertible):
		super().__init__(color, maxSpeed)
		self.numGears = numGears
		self.isConvertible = isConvertible

	def printCar(self):
		print("Color: ", self.color)
		print("Max Speed: ", self.getMaxSpeed())
		print("Num of Gears: ", self.numGears)
		print("Is Convertable: ",  self.isConvertible)

c = Car("red", 15 , 3 , False)
c.printCar()


#better way is to put the printing of members of different classes in their respective classes
print("\n\n\n\n")

class betterWayVehicle:
	def __init__(self, color, maxSpeed):
		self.color = color
		self.__maxSpeed = maxSpeed

	def getMaxSpeed(self):
		return self.__maxSpeed

	def setMaxSpeed(self, maxSpeed):
		self.__maxSpeed = maxSpeed

	def print(self):
		print("Color :", self.color)
		print("Max Speed :", self.__maxSpeed)


class betterCar(betterWayVehicle):
	def __init__(self, color, maxSpeed, numGears, isConvertible) :
		super().__init__(color, maxSpeed)
		self.numGears = numGears
		self.isConvertible = isConvertible

	def printCar(self):
		super().print()
		print("Num Gears :", self.numGears)
		print("Is Convertable :", self.isConvertible)

c = betterCar("Green", 15, 3, False)
c.printCar()


		