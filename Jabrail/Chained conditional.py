x = int(input("enter your score:"))
if (x < 101 and x > 0):
    if x > 89:
        print("A")
    elif x > 79:
        print("B")
    elif x > 69:
        print("c")
    elif x > 59:
        print("d")
    else:
        print("f")
else:
    print("you are out of range")
