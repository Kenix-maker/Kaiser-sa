sum = 0
diff = 0
numbers = {1 : "one", 2 : "two", 3 : "three", 4 : "four"}
for i in range(1, 3):
    num = int(input("Number value {}: ".format(numbers[i])))
    sum += num
for i in range(3, 5):
    num = int(input("Number value {}: ".format(numbers[i])))
    if diff == 0:
        diff = num
    else:
        diff -= num

concatenate = str(sum) + str(diff)
print("Output:", concatenate)

