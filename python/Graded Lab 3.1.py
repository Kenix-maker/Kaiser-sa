def check_range(num):
    if num >= 1 and num <= 10:
        print("Number ranges between 1 and 10")
    else:
        print("Number does not range between 1 and 10")

while True:
    n = int(input("Enter a number to check range: "))
    check_range(n)
