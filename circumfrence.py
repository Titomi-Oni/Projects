def circumference(radius):
    pi = 3.14
    return 2 * pi * radius

radius = float(input("Enter the radius of the circle: "))

answer = circumference(radius)
print("The circumference is:", answer)