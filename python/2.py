house = str(input("Do you have a house (Y/N): "))
car = str(input("Do you own a car (Y/N): "))
salary = int(input("How much do you earn: "))
relationship = str(input("Are you married (Y/N): "))

if house.lower() == "y" and car.lower() == "y" and salary >= 50000 and relationship.lower() == "n":
	print("You are eligible to date Lesego")
else:
	print("You are not eligible to date Lesego")