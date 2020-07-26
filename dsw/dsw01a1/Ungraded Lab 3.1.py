def details():
	full_names = str(input("Enter your full names: "))
	surname = str(input("Enter your surname: "))
	id_No = int(input("Enter your id number: "))
	concan = full_names + " " + surname
	print("Name & Surname:", concan, "\nId No.:", id_No)

details()
