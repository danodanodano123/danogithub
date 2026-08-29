Number=float(input("Enter your number: "))
if Number<=0:
    print("Error!")
elif Number>0:
    Number=Number%2
    if Number==0:
        print("Even number")
    else:
        print("Odd number")