n = int(input("Enter a numer to get multiples of: "))
for i in range(1, 101):
    print("{} * {} = {}".format(n, i, (n * i)))
