next = True
sum = 0
while next:
	num = int(input("Enter a number: "))
	sum += num
	user = str(input("do you want to continue?"))
	if user.lower() == "yes":
		next = True
	else:
		next = False

print("Your total of numbers added is", sum)