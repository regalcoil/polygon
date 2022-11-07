import math

def polygon():
	print(" ")
	sides = int(input("How many sides does your equilateral polygon have? "))
	if sides < 3:
		print(" ")
		print("Sorry, please enter a number greater than 2")
		print(" ")
		print("**************")
		polygon()
	angle = 360/(sides*2)
	print(" ")
	length = float(input("What is the length of each side? "))
	radians = math.radians(angle)
	radius = (length/2) / math.tan(radians)
	triA = ((length/2) * radius)/2
	Area = triA*(sides*2)
	print(" ")
	print("Area: " + str(Area) + " units^2")
	print(" ")
	print("**************")
	polygon()

polygon()