a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

x1 = (-b + ((b**2) - (4*a*c))**1/2) / (2*a)
x2 = (-b - ((b**2) - (4*a*c))**1/2) / (2*a)
print("{}x^2 + {}x + {}\nx1 = {} and x2 = {}".format(a, b, c, x1, x2))