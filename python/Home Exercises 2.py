f = int(input("Enter temperature: "))
c = (f - 32) * 5/9
if c > 28:
    print("It is hot")
elif c < 20:
    print("It is cold")
else:
    print("it is normal")
