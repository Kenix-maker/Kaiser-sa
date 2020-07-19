number = int(input("Tshepo enter a number: "))

if number > 3:
	for i in range(2, number//2 + 1):
		if number % i == 0:
			print(number,"is not a prime number")
			break
		else:
			print(number, "is a prime number")
			break
else:
	print(number, "is a prime number")