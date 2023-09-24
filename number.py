x=int(input("Enter a 4 digit number;"))
y=x//1000
print("thousand-",y)
h=x//100%10
print("hundreds-",h)
t=x//10%10
print("Tens-",t)
p=x//1%10
print("Units-",p)

print(y+h+t+p)