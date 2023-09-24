number=int(input("Enter a random number:"))
last_digit=number%10
if number%5 and number%3==0:
    print("The number is divisble by 6!")
else:
    print("The number is not divisible by 6!")