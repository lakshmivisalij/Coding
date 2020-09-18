class ZeroDenomError(ZeroDivisionError):
	pass

try:

	num = int(input("Enter Numerator: "))
	denom = int(input("Enter Denominator: "))
	if denom == 0:
		raise ZeroDenomError


	val = num/denom
    

except ZeroDivisionError:
	print('In built ZeroDivisionError')
except ZeroDenomError:
	print("Zero in Denominator, custom ")

except:
	print('Any other exception might have raised')

else:
	#executes only if no exception has occured
	print("Numerator: ",num)
	print("Denominator: ",denom)
	print(val)

finally:
	print("Numerator: ",num)
	print("Denominator: ",denom)
	print(val)
	print("Finally is executed always")