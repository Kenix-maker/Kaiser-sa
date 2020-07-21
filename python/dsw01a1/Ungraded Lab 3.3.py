total = 0
for i in range(1, 6):
	grade = int(input("Enter grade ({}) of 5: ".format(i)))
	total += grade

avg = total / 5

if avg > 60:
	print("Passed with an average of {}%".format(avg))
else:
	print("Failed with an average of {}%".format(avg))