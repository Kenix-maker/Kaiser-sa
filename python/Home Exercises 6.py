from datetime import date

id_num = str(input("Enter your id number: "))
today = date.today().year
if (int(str(today)[2:]) - int(str(id_num)[:2])) > 18:
    print("You are old enough to vote")
else:
    print("you are not old enough to vote")
