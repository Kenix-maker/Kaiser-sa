x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x > y:
	print("{} is greater than {}".format(x, y))
elif y > x:
	print("{} is greater than {}".format(y, x))
else:
	print("{} and {} are equal".format(x, y))