#Write a Python program to find whether a given number (accept from the user) is
#even or odd, print out an appropriate message to the user.
num=int(input("Enter a number:"))
rey=num%2
if rey==0:
    print(num,"is an even number")
elif rey==1:
    print(num,"is an odd number")