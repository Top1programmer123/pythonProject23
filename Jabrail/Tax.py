x = int(input("What is the bikes price:"))

if (x > 100000):
    print(x * 0.15 + x)
elif (x > 50000 and x <= 100000):
    print(x * 0.1 + x)
elif (x <= 50000):
    print(x * 0.05 + x)
