age = int(input("Enter your age: "))
if age >= 0 and age <= 3:
    print("Infant")
elif age >= 4 and age <= 11:
    print("Child")
elif age >= 12 and age <= 17:
    print("Teenager")
else:
    print("Adult")
