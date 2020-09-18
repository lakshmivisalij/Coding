while 1:
	try:
		num = int(input("Enter numerator: "))
		den = int(input("Enter denominator: "))

		val = num/den

		print(val)

		break
	except(ValueError, ZeroDivisionError):
		print("numerator and denominator should be integers and denominator shouldn't be zero")
	except(ZeroDivisionError):
	    print("denominator shouldn't be zero")