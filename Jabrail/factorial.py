def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x - 1)


x = int(input("Enter x"))
if x < 0:
    print("This is a negative number")
elif x == 0:
    print("Factorial is 0")
else:
    print("Factorial of", x, "is:", factorial(x))
