def sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

num = int(input("Enter a number: "))
print("Your sum of numbers is", sum(num))
