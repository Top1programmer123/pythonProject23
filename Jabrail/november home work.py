x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))

if x == y == z:
    print("equal triangle")
elif x == y or y == z or z == x:
    print("isoceles triangle")
else:
    print("Scalene triangle")
