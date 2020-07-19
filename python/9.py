a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

x1 = ((-1*b) + (((b**2) - (4*a*c))**1/2)) / (2*a)
x2 = ((-1*b) - (((b**2) - (4*a*c))**1/2)) / (2*a)

print("Input:\na = {0} b = {1} c = {2}\nOutput:\nx1 = {3} and x2 = {4}".format(a, b, c, x1, x2))