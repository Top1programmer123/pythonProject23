# def Division(a,b):

#   print(int(a/b))

# Division(24,8)

def even_or_odd(a):
    if (a % 2 == 0):
        print("its even")
        return a
    else:
        print("its odd")
        return 1


def multiplication(b):
    c = even_or_odd(b) * 3
    print(c)


multiplication(3)
