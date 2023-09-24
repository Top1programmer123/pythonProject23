x=int(input("Enter your number:"))
y=0
z=1
q=1
while x>0:
    n=int(input("Enter number:"))
    y=y+n
    z=n*z
    q=n/q
    x=x-1
print(y)
print(z)
print(q)
