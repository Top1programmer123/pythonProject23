x = int(input()) // 1000
y = int(input('Input y'))
print("thousand-", y)
h = x // 100 % 10
print("hundreds-", h)
t = x // 10 % 10
print("Tens-", t)
p = x // 1 % 10
print("Units-", p)
