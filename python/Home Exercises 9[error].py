from random import randint

user = int(input("1.Rock\n2.Paper\n3.Scissors\n(1/2/3): "))
cpu = randint(1, 3)

while cpu == user:
    cpu = randint(1, 3)

if ((user == 1 and cpu == 3) or (user == 3 and cpu == 1)):
    print("rock wins")

elif ((user == 2 and cpu == 1) or (user == 1 and cpu == 2)):
    print("paper wins")

elif ((user == 3 and cpu == 2) or (user == 2 and cpu == 3)):
    print("scissors wins")

else:
    print("its a draw")
