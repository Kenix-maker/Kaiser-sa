n = int(input("Enter the limit of your negtive sequence: "))

for i in range(n + 1, 0, -1):
	if i == 1:
		print(i)
	else:
		print(i, end=", ")