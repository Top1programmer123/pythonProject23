x = int(input("Enter your age:"))
y = int(input("enter your BMI:"))

if (x < 45 and y < 22):
    print("your heart disease risk is Low")


elif (x < 45 and y >= 22):

    print("your risk of a heart disease is medium")

elif (x >= 45 and y < 22):
    print("Your risk of a heart disease is medium")


elif (x >= 45 and y >= 22):
    print("You risk of a heart disease is high so look after yourself")
