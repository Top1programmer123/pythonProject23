def three_values(a,b,c):
    if (a>b) and (a>c):
        print("a is the biggest",a )
    elif (b>a) and (b>c):
        print('b is the biggest ',b)
    elif (c>a) and (c>b):
        print("c is the biggest", c)
    else:
        print("they are equal")

three_values (int(input("c")),int(input("b")),int(input("a:")))