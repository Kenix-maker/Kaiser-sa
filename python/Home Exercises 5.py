cost = float(input("Enter total cost of treatment: "))
discount = cost - (cost * 0.25)
pensioner = str(input("Are you a pensioner? (Y/N): "))
if pensioner.lower() == "y":
    print("Congrats!! You get a 25% off, your new total cost of treatment is", discount)
else:
    print("Your total cost of treatment is", cost)
