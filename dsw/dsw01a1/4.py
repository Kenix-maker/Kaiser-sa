n = int(input("How many numbers do you want to add?: " ))
sum = 0

for i in range(1, n + 1):
	num = int(input("Enter number you want to add: "))
	sum += num

print("sum of {} is {}".format(n, sum))

OR

n = int(input("How many numbers do you want to add?: " ))
sum = 0

for i in range(1, n + 1):
	sum += i

print("sum of {} is {}".format(n, sum))