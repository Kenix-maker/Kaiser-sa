def surface(l, w, h):
    A = (2*w*l) + (2*l*h) + (2*h*w)
    return A

width = float(input("Enter width of rectangle: "))
length = float(input("Enter length of rectangle: "))
height = float(input("Enter height of rectangle: "))
surface_of_rectangle = surface(length, width, height)
print("surface of rectangle is", surface_of_rectangle)
