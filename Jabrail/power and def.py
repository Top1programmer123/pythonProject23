def power(x, tip):
    if not (x == 1) or (x == 0):
        tip = power(x - 1, tip) * x

    elif x == 0:
        return 1
    else:
        return tip


def powers(x):
    output = 1
