import random
num=random.randrange(1,10)

while True:
    guess=int(input("Enter a number: "))
    if guess==num:
        print("You guessed the number!")
        break
    if guess>num:
        print("Too high!")
    if guess<num:
        print("Too low!")