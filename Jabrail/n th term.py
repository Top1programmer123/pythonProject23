def nth_term(n):
    n = int(input("Enter n:"))
    x = n ** 2 + 1
    return (x)


answer = nth_term(5) + 2 * nth_term(5) + 64
print(answer)
